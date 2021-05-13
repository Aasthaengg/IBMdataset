from collections import deque

N, M = map(int, input().split())
ans = 0
roads = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
  G = [[]*N for _ in range(N)]
  for j in range(M):
    if j == i:
      continue
    a, b = roads[j]
    G[a-1].append(b-1)
    G[b-1].append(a-1)
  
  stack = deque([0])
  visited = [False] * N
  visited[0] = True
  while stack:
    now = stack.pop()
    for nxt in G[now]:
      if visited[nxt]:
        continue
      visited[nxt] = True
      stack.append(nxt)
      
  for f in visited:
    if not f:
      ans += 1
      break
      
print(ans)
