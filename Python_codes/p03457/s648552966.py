n=int(input())
dt,dx,dy=0,0,0
for i in range(n):
  t,x,y=map(int,input().split())
  if abs(x-dx) + abs(y-dy) > t-dt or (x+y)%2!=t%2:
    print("No")
    break
  dt,dx,dy=t,x,y
else:
  print("Yes")