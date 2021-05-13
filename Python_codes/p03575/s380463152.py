from collections import deque
from copy import deepcopy

n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]

def BFS(m):
  t_l=deepcopy(l)
  del t_l[m]

  tree=[[] for j in range(n)]
  for a,b in t_l:
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)

  dist=[-1 for i in range(n)]
  dist[0]=0

  que=deque()
  que.append(0)

  while que:
    x=que.popleft()
    for i in tree[x]:
      if dist[i]==-1:
        que.append(i)
        dist[i]=dist[x]+1

  global ans
  if -1 in dist:
    ans+=1

ans=0
for i in range(m):
  BFS(i)

print(ans)