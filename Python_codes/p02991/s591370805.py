from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(3*N)]
for _ in range(M):
  u, v = map(lambda x:int(x)-1, input().split())
  graph[3*u] += [3*v+1]
  graph[3*u+1] += [3*v+2]
  graph[3*u+2] += [3*v]

S, T = map(lambda x:int(x)-1, input().split())

def bfs(s):
  q = deque([s])
  dist = [float('inf')]*(3*N)
  dist[s] = 0

  while q:
    u = q.popleft()
    for v in graph[u]:
      if dist[v] == float('inf'):
        q += [v]
        dist[v] = dist[u] + 1

  return dist

d = bfs(3*S)
if d[3*T] == float('inf'):
  print(-1)
else:
  print(d[3*T]//3)