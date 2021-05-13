from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = tuple(map(lambda x: int(x)-1, input().split()))
  G[a].append(b)
  G[b].append(a)

color = [0]*N
color[0] = 1
color[N-1] = -1
q = deque([])
q.append(0)
q.append(N-1)

while q:
  node = q.popleft()
  c = color[node]
  for to in G[node]:
    if color[to] == 0:
      color[to] = c
      q.append(to)

b = color.count(1)
w = color.count(-1)

if b > w:
  print('Fennec')
else:
  print('Snuke')