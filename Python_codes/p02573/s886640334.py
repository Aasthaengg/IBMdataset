n, m = list(map(int, input().split()))
relations = {}
for _ in range(m):
  a, b = list(map(int, input().split()))
  a -= 1
  b -= 1
  if relations.get(a):
     relations[a].append(b)
  else:
    relations[a] = [b]
  if relations.get(b):
    relations[b].append(a)
  else: 
    relations[b] = [a]

from collections import deque
visited = [False for i in range(n)]

groups = 0
def bfs(n, visited):
  global groups
  queue = deque([n])
  group_len = 0
  while queue:
    current = queue.popleft()
    if not visited[current]:
      visited[current] = True
      if relations.get(current):
        for neighbor in relations[current]:
          queue.append(neighbor)
        group_len += 1

  groups = max(groups, group_len)
    

if m == 0:
  print(1)
else:
  for i in range(n):
    if not visited[i]:
      bfs(i, visited)

  print(groups)