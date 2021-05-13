x,y=map(int,input().split())
if x%y==0:
  exit(print(-1))
t=0
for i in range(1000001):
  t+=x
  if t%y!=0:
    print(t)
    exit(0)
