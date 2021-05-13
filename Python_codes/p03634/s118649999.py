from collections import *
import sys
S=sys.stdin.readlines()
N=int(S[0])
G=[[] for i in range(N)]
a,b,c=0,0,0
for i in range(N-1):
  a,b,c=map(int,S[i+1].split())
  a,b=a-1,b-1
  G[a].append((b,c))
  G[b].append((a,c))
Q,K=map(int,S[N].split())
D,Z=deque(),set()
def qao(x):
  global D,Z
  if x in Z:
    return False
  Z.add(x)
  D.append(x)
  return True

dist=[0]*N
def bfs():
  global dist,D,G
  v=0
  for i in range(len(D)):
    v=D.popleft()
    for j in range(len(G[v])):
      if qao(G[v][j][0]):
        dist[G[v][j][0]]=G[v][j][1]+dist[v]
  return len(D)

qao(K-1)
while bfs():
  pass
for i in range(Q):
  a,b=map(int,S[N+1+i].split())
  print(dist[a-1]+dist[b-1])