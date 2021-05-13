f=lambda:map(int,input().split())
n,k,l=f()
def root(x):
  while p[x]>=0: x=p[x]
  return x
def unite(x,y):
  x,y=root(x),root(y)
  if x==y: return
  if x>y: x,y=y,x
  p[x]+=p[y]
  p[y]=x
def g(x):
  global p
  p=[-1]*n
  for _ in range(x):
    a,b=f()
    unite(a-1,b-1)
  return [root(i) for i in range(n)]
H,R=g(k),g(l)
from collections import *
z=[*zip(H,R)]
C=Counter(z)
print(*[C[t] for t in z])