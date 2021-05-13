n,Y=map(int,input().split())

ans=0
for x in range(0,n+1):
  if ans>0:
    break
  for y in range(0,n+1-x):
    z=n-x-y
    if 10000*x+5000*y+1000*z==Y:
      ans+=1
      print(str(x)+' '+str(y)+' '+str(z))
      
    if ans>0:
      break
      
if ans==0:
  print(str(-1)+' '+str(-1)+' '+str(-1))