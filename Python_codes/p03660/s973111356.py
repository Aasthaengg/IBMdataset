N=int(input())
graph=[[] for i in range(N)]
for i in range(N-1):
  a,b=map(int,input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)
from collections import deque  
def dfs(k):
  visited=[-1 for i in range(N)]
  visited[k]=0
  q=deque([])
  q.append(k)
  while q:
    u=q.popleft()
    for v in graph[u]:
      if visited[v]==-1:
        visited[v]=visited[u]+1
        q.append(v)
  return visited
a=dfs(0)
b=dfs(N-1)
count=0
for i in range(N):
  if a[i]<=b[i]:
    count+=1
if count>N//2:
  print("Fennec")
else:
  print("Snuke")