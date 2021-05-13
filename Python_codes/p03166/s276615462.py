from sys import setrecursionlimit
setrecursionlimit(1<<30)
def f(x):
  if z[x]==-1:
  	z[x]=max([f(i) for i in v[x]]+[-1])+1
  return z[x]
n,m=map(int,raw_input().split())
v=[[] for _ in xrange(n)]
for x,y in [map(int,raw_input().split()) for _ in xrange(m)]:
  v[x-1].append(y-1)
z=[-1]*n
for i in xrange(n):
  if z[i]==-1:
    f(i)
print max(z)