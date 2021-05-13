from collections import deque
h, w = map(int,input().split())
maze = [[i for i in input()] for _ in range(h)] # h * w
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
  dist = [[-1] * w for _ in range(h)]
  d = deque()
  d.append((i, j))
  dist[i][j] = 0
  ret = 0
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
  for i in range(h):
    for j in range(w):
      if ret < dist[i][j]:
        ret = dist[i][j]
  return ret

ans = 0
for i in range(h):
  for j in range(w):
    if maze[i][j] == "#":
      continue
    d = bfs(i, j)
    if ans < d:
      ans = d

print(ans)

