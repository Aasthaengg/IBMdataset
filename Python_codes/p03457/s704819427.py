N=int(input())
t0=0
x0=0
y0=0
 
for i in range(N):
  t1,x1,y1=map(int,input().split())
  AbsT=t1-t0
  AbsX=abs(x1-x0)
  AbsY=abs(y1-y0)
  if AbsX+AbsY>AbsT or (AbsX+AbsY-AbsT)%2!=0:
    print("No")
    break
  else:
      x0=x1
      y0=y1
      t0=t1

else:
  print("Yes")