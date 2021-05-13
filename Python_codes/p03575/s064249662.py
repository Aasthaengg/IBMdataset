from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

cand = []
for _ in range(m):
  a, b = map(int, input().split())
  cand.append((a-1, b-1))
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

def bfs(i):
  dist = [-1] * n
  dist[i] = 0
  d = deque()
  d.append(i)
  while d:
    v = d.popleft()
    for j in graph[v]:
      if dist[j] != -1:
        continue
      dist[j] = dist[v] + 1
      d.append(j)
  return dist

def judge(c):
  graph[c[0]].remove(c[1])
  graph[c[1]].remove(c[0])
  dist = bfs(0)
  graph[c[0]].append(c[1])
  graph[c[1]].append(c[0])
  for d in dist:
    if d == -1:
      return True
  return False

ans = 0
for c in cand:
  if judge(c):
    ans += 1
print(ans)

