from collections import *
N,K,L = map(int,input().split())

def root(x):
  while 0<=p[x]:
    x = p[x]
  return x

def unite(x,y):
  x = root(x)
  y = root(y)
  if x==y:
    return
  if x>y:
    x,y=y,x
  p[x]+=p[y]
  p[y]=x

def g(x):
  global p
  p=N*[-1]
  for _ in range(x):
    a,b = map(int,input().split())
    unite(a-1,b-1)
  return [root(n) for n in range(N)]

z = [*zip(g(K),g(L))]
C = Counter(z)
print(*[C[t] for t in z])