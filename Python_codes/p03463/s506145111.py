n,a,b=map(int,input().split())
a-=1
b-=1
while 1:
  if a+1==b:
    if a==0:
      print("Borys")
      break 
    a-=1
  else:
    a+=1
  
  if b-1==a:
    if b==n-1:
      print("Alice")
      break
    b+=1
  else:
    b-=1