f=lambda:map(int,input().split())
def r(x):
  while p[x]>=0: x=p[x]
  return x
def u(x,y):
  x,y=r(x),r(y)
  if x==y: return
  if x>y: x,y=y,x
  p[x]+=p[y]
  p[y]=x
n,m=f()
p=[-1]*n
for _ in range(m):
  a,b=f()
  u(a-1,b-1)
print(sum(i<0 for i in p)-1)