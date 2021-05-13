from collections import deque
 
def dfs(n, start, graph):
  visited = [False] * n
  stack = deque()
  stack.append(start)
  visited[start] = True
  while stack:
    q = stack.popleft()
    nxts = graph[q]
    for nxt in nxts:
      if not visited[nxt]:
        visited[nxt] = True
        stack.append(nxt)
  return visited
 
n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
 
ans = 0
for i in range(m):
  graph = [[] for _ in range(n)]
  for itr, (a, b) in enumerate(edge):
    if itr != i:
      graph[a - 1].append(b - 1)
      graph[b - 1].append(a - 1)
 
  if not all(dfs(n, 0, graph)):
    ans += 1
print(ans)