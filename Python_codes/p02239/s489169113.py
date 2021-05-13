from collections import deque
from enum import Enum

class Color(Enum):
  WHITE = 0
  GRAY = 1
  BLACK = 2


N = int(input())
adj = [list(map(int, input().split()))[2:] for i in range(N)]


colors = [Color.WHITE for i in range(N)]
INF = N
d = [-1 for i in range(N)]
d[0] = 0

q = deque()
q.append(1)
colors[0] == Color.GRAY
while len(q) > 0:
  u = q.popleft()-1
  for v in adj[u]:
    v -= 1
    if colors[v] != Color.WHITE:
      continue
    d[v] = d[u] + 1
    colors[v] = Color.GRAY
    q.append(v+1)
  colors[u] = Color.BLACK

for i in range(N):
  print(i+1, d[i])
