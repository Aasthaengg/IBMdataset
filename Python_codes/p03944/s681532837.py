W,H,N=map(int,input().split())

a1,a2,a3,a4=0,W,0,H
for i in range(N):
  x,y,a=map(int,input().split())
  if a==1:a1=max(a1,x)
  elif a==2:a2=min(a2,x)
  elif a==3:a3=max(a3,y)
  else:a4=min(a4,y)
    
if a1>=a2 or a3>=a4:
  print(0)
  exit()
if a1>=W or a2<=0 or a3>=H or a4<=0:
  print(0)
  exit()
  
print((a2-a1)*(a4-a3))