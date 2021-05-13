import sys
from collections import *
S=sys.stdin.readlines()
N,Q=map(int,S[0].split())
G=[[] for i in range(N)]
a,b=0,0
for i in range(N-1):
  a,b=map(int,S[i+1].split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
X=[0]*N
for i in range(Q):
  a,b=map(int,S[N+i].split())
  X[a-1]+=b
D=deque()
S=set()
def qao(x):
  global D,S
  if x in S:
    return False
  S.add(x)
  D.append(x)
  return True

def bfs():
  global D,X,G
  v=0
  for i in range(len(D)):
    v=D.popleft()
    for j in range(len(G[v])):
      if qao(G[v][j]):
        X[G[v][j]]+=X[v]
  return len(D)

qao(0)
while bfs():
  pass
print(*X)