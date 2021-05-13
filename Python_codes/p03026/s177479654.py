from collections import deque
n=int(input())
d=dict()
edge=[[] for _ in range(n)]
for _ in range(n-1):
  a,b=map(int,input().split())
  a-=1
  b-=1
  edge[a].append(b)
  edge[b].append(a)
c=list(map(int,input().split()))
c.sort(reverse=True)
visited=[-1]*n
def bfs(s):
  i=0
  q=deque([s])
  visited[s]=c[i]
  while q:
    x=q.popleft()
    for nx in edge[x]:
      if visited[nx]==-1:
        i+=1
        visited[nx]=c[i]
        q.append(nx)
  return
bfs(0)
print(sum(c)-max(c))
print(*visited)