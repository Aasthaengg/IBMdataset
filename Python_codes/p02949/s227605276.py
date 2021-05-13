from collections import deque
n,m,p=map(int,input().split())
edges=[None for i in range(m)]
natural=[[] for i in range(n)]
reverse=[[] for i in range(n)]
for i in range(m):
  a,b,c=map(int,input().split())
  a-=1;b-=1;c-=p
  natural[a].append(b)
  reverse[b].append(a)
  edges[i]=(a,b,-c)
from0=set([0])
fromG=set([n-1])
visited=[False]*n
visited[0]=True
queue=deque([0])
while queue:
  v=queue.popleft()
  for i in natural[v]:
    if visited[i]:continue
    visited[i]=True
    from0.add(i)
    queue.append(i)
for i in range(n):
  visited[i]=False
visited[-1]=True
queue.append(n-1)
while queue:
  v=queue.popleft()
  for i in reverse[v]:
    if visited[i]:continue
    visited[i]=True
    fromG.add(i)
    queue.append(i)
points=from0&fromG
use=[]
for i in edges:
  if i[0] in points and i[1] in points:
    use.append(i)
def BellmanFord(edges,num_v,source):
  #グラフの初期化
  inf=10**15
  global dist
  dist=[inf for i in range(num_v)]
  dist[source]=0
  Ncycle=False
  #辺の緩和
  for i in range(num_v):
    for edge in edges:
      if edge[0]!=inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        if i==num_v-1: return False
  
  return dist[-1]
flag=0
for i in use:
  if i[2]!=0:
    flag=1
    break
if flag==0:print(0);exit()
if BellmanFord(use,n,0)==False:print(-1)
else:
  print(max(0,-BellmanFord(use,n,0)))
