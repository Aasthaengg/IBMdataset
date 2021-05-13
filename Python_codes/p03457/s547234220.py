N=int(input())
x0,y0=0,0
t0=0
for n in range(N):
  t,x,y=map(int,input().split())
  if abs(x-x0)+abs(y-y0) > t-t0:
    print('No')
    exit(0)
  if (abs(x-x0)+abs(y-y0))%2 != (t-t0)%2:
    print('No')
    exit(0)
  t0,x0,y0=t,x,y
print('Yes')