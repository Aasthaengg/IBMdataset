N=int(input())
x,y=0,0
time=0
for i in range(N):
  t,a,b=map(int,input().split())
  if abs(x-a)+abs(y-b)>t-time or (abs(x-a)+abs(y-b)-t+time)%2==1:
    print("No")
    exit()
  time=t
  x=a
  y=b
print("Yes")