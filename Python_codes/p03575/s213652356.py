import sys
sys.setrecursionlimit(1000000000)
N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)]
visited = [0]*N
ab = []
ans = 0

def dfs(u):
  visited[u] = 1
  for v in range(N):
    if graph[u][v] == 1 and visited[v] == 0:
      dfs(v)

for _ in range(M):
  a, b = map(lambda x:int(x)-1, input().split())
  graph[a][b] = 1
  graph[b][a] = 1
  ab += [[a, b]]

for _ in range(M):
  a, b = ab.pop(0)
  graph[a][b] = 0
  graph[b][a] = 0

  for i in range(N):
    visited[i] = 0
  
  dfs(0)
  
  if sum(visited) != N:
    ans += 1

  graph[a][b] = 1
  graph[b][a] = 1

print(ans)