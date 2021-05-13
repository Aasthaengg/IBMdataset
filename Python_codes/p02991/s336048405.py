from collections import deque

N, M = map(int, input().split())

graph = [[] for i in range(3*N)]
for i in range(M):
  u, v = map(int, input().split())
  u, v = 3*(u - 1), 3*(v - 1)
  graph[u].append(v+1)
  graph[u+1].append(v+2)
  graph[u+2].append(v)

s, t = map(int, input().split())
s, t = 3*(s - 1), 3*(t - 1)


dist = [10**9] * 3*N
dist[s] = 0
d = deque([s])
while d:
  node = d.popleft()
  children = graph[node]
  for child in children:
    if dist[child] > dist[node] + 1:
      d.append(child)
      dist[child] = dist[node] + 1

if dist[t] < 10**9:
  print(dist[t]//3)
else:
  print(-1)