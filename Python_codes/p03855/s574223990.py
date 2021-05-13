from collections import Counter
N,K,L=map(int,input().split())

def root(x):
  while p[x]>=0:
    x=p[x]
  return x

def unite(x,y):
  x,y=root(x),root(y)
  if x==y: return
  if x>y: x,y=y,x
  p[x]+=p[y]
  p[y]=x

def g(x):
  global p
  p=[-1]*N
  for _ in range(x):
    a,b=map(int,input().split())
    unite(a-1,b-1)
  return [root(i) for i in range(N)]

z=[*zip(g(K),g(L))]
cnt=Counter(z)
print(*[cnt[t] for t in z])