l=lambda:map(int, input().split())
n,m=l()
p=[-1]*n
def root(x):
  if p[x]<0:return x
  p[x]=root(p[x]);return p[x]
def union(x,y):
  x,y=root(x),root(y)
  if x==y: return
  p[x]+=p[y]
  p[y]=x
def same(x,y):
  return root(x)==root(y)
def size(x):
  return -p[r(x)]
for _ in range(m):
  a,b=l()
  union(a-1,b-1)
print(-min(p))