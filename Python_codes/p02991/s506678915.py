import sys
from collections import *
I=sys.stdin.readlines()
N,M=map(int,I[0].split())
E=[]
for i in range(M):
  E.append(list(map(lambda x:x-1,(list(map(int,I[i+1].split()))))))
S,T=map(int,I[M+1].split())
G=[[] for i in range(3*N)]
for i in range(M):
  G[E[i][0]].append(E[i][1]+N)
  G[E[i][0]+N].append(E[i][1]+N+N)
  G[E[i][0]+N+N].append(E[i][1])
D=deque()
Z=set()
def qao(x):
  global D,Z
  if x in Z:
    return False
  D.append(x)
  Z.add(x)
  return True

def bfs():
  global D,G,N
  v=0
  for i in range(len(D)):
    v=D.popleft()
    for j in range(len(G[v])):
      qao(G[v][j])
  return len(D)==0

qao(S-1)
for i in range(3*N):
  bfs()
  if T-1 in Z:
    print((i+1)//3)
    exit()
print(-1)