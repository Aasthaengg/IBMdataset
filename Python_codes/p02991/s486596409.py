from collections import deque
n,m=map(int,input().split())
if m==0:
  print(-1)
  exit()
edge=[[] for i in range(3*n)]
for i in range(m):
  u,v=map(int,input().split())
  edge[3*(u-1)].append(3*(v-1)+1)
  edge[3*(u-1)+1].append(3*(v-1)+2)
  edge[3*(u-1)+2].append(3*(v-1))
s,t=map(int,input().split())
s-=1
t-=1
visited=[0 for i in range(3*m)]
def bfs(edge,visited,s,t):
  q=deque([3*s])
  visited[3*s]=1
  cnt=0
  while q:
    x=q.popleft()
    if x%3==0 and x//3==t:
      return visited[x]//3
    for i in edge[x]:
      newx=i
      if visited[newx]==0:
        visited[newx]=visited[x]+1
        q.append(newx)
  return -1
print(bfs(edge,visited,s,t))