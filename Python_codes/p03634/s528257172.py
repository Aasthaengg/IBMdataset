N=int(input())
tree=[[] for i in range(N)]
for i in range(N-1):
  a,b,c=map(int,input().split())
  tree[a-1].append((b-1,c))
  tree[b-1].append((a-1,c))
from collections import deque
visited=[-1 for i in range(N)]
Q,K=map(int,input().split())
visited[K-1]=0
q=deque([])
q.append(K-1)
while q:
  u=q.popleft()
  for v,d in tree[u]:
    if visited[v]==-1:
      visited[v]=visited[u]+d
      q.append(v)
    
for i in range(Q):
  x,y=map(int,input().split())
  print(visited[x-1]+visited[y-1])