h, w = map(int, input().split())
maze = [[i for i in input()] for _ in range(h)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dist = [[-1] * w for _ in range(h)]
dist[0][0] = 0
from collections import deque
d = deque()
d.append((0, 0))

count = 0
for i in range(h):
  for j in range(w):
    if maze[i][j] == ".":
      count += 1

while d:
  x, y = d.popleft()
  for m in move:
    i = x + m[0]
    j = y + m[1]
    if i >=0 and i < h and j >= 0 and j < w:
      if maze[i][j] == "#":
        continue
      if dist[i][j] != -1:
        continue
      dist[i][j] = dist[x][y] + 1
      d.append((i, j))
mindist = dist[h-1][w-1]
if mindist == -1:
  print(-1)
else:
  print(count-mindist -1)
