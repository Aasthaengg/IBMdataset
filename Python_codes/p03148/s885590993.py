from heapq import *
import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readlines()
N,K=map(int,I[0].split())
t,d=0,0
X=[]
for i in range(N):
  t,d=map(int,I[i+1].split())
  X.append((d,t))
X.sort()
Q=[]
heapify(Q)
C=[0]*N
V=0
S=0
for i in range(K):
  heappush(Q,X[-1])
  if C[X[-1][1]-1]==0:
    V+=1
  S+=X[-1][0]
  C[X[-1][1]-1]+=1
  del X[-1]
def f(q,c,s,x,v):
  y=0
  r=s+v*v
  for i in range(len(q)):
    y=heappop(q)
    if c[y[1]-1]>=2:
      s-=y[0]
      c[y[1]-1]-=1
      break
    if len(q)==0:
      return r
  for i in range(len(x)):
    if c[x[-1][1]-1]==0:
      heappush(q,x[-1])
      s+=x[-1][0]
      c[x[-1][1]-1]=1
      v+=1
      del x[-1]
      return max(r,f(q,c,s,x,v))
    del x[-1]
  return r
print(f(Q,C,S,X,V))