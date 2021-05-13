import sys
readline = sys.stdin.buffer.readline

from collections import deque

N, M = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())
INF = 10 ** 15

if M == 0:
  print(-1)
  exit()

graph = [[] for _ in range(3 * M + 1)]
for u, v in UV:
  graph[u].append(v + M)
  graph[u + M].append(v + 2 * M)
  graph[u + 2 * M].append(v)

queue = deque([S])
dist = [INF] * (3 * M + 1)
dist[S] = 0

while queue:
  q = queue.popleft()
  for g in graph[q]:
    if dist[g] > dist[q] + 1:
      dist[g] = dist[q] + 1
      queue.append(g)
print(dist[T] // 3 if dist[T] != INF else -1)