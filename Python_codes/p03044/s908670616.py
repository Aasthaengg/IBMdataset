from collections import deque

def dfs(start):
  stack = deque([[start, 0]])
  while stack:
    p, c = stack.popleft()
    for next, distance in graph[p]:
      if visited[next] == -1:
        if distance % 2 == 0:
          visited[next] = int(c)
        else:
          visited[next] = int(not c)
        stack.append([next, visited[next]])

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1):
  a, b, w = map(int, input().split())
  graph[a - 1].append([b - 1, w])
  graph[b - 1].append([a - 1, w])

visited = [-1] * n
visited[0] = 0
dfs(0)
for v in visited:
    print(v)