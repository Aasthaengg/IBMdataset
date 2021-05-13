n=int(input())
G=[[] for i in range(n)]
for i in range(n-1):
  u,v,w=map(int,input().split())
  G[u-1].append([v-1,w])
  G[v-1].append([u-1,w])
dist=[-1]*n
from collections import deque
Q,k=map(int,input().split())
q=deque()
q.append(k-1)
dist[k-1]=0
while q:
  cur=q.popleft()
  for nx,nd in G[cur]:
    if dist[nx]!=-1:continue
    dist[nx]=dist[cur]+nd
    q.append(nx)
for i in range(Q):
  x,y=map(int,input().split())
  x-=1
  y-=1
  print(dist[x]+dist[y])
