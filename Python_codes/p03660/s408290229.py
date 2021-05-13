n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
  a, b = (int(x)-1 for x in input().split())
  graph[a].append(b)
  graph[b].append(a)

from collections import deque
def bfs(s:int)->list:
  dist = [-1]*n
  dist[s] = 0
  que = deque([s])
  while que:
    u = que.popleft()
    for v in graph[u]:
      if dist[v] != -1: continue
      dist[v] = dist[u] + 1
      que.append(v)
  return dist

dfen = bfs(0)
dsnu = bfs(n-1)
pfen = 0
psnu = 0
for i in range(n):
  if dfen[i] <= dsnu[i]: pfen += 1
  else: psnu += 1
ans = 'Fennec' if pfen > psnu else 'Snuke'
print(ans)
