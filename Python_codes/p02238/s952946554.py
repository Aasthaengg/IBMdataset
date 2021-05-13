from collections import deque
n = int(input())
graph = [deque([]) for _ in range(n+1)]
ans = [[i, ] for i in range(n+1)]
for i in range(n):
  u, k, *v = list(map(int, input().split()))
  for j in v:
    graph[u].append(j)
stack = deque()
stack.append(1)
marked = []
t = 0
def dfs(v):
  global t
  marked.append(v)
  t += 1
  ans[v].append(t)
  for i in graph[v]:
    if i in marked:
      continue
    else:
      marked.append(i)
      dfs(i)
  t += 1
  ans[v].append(t)
for i in range(1, n+1):
  if len(ans[i])==1:
    dfs(i)
for i, x in enumerate(ans):
  if i==0:
    continue
  print(*x)
