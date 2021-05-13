from collections import deque
H, W = map(int, input().split())
que = deque()
A = [input() for i in range(H)]

dist = [[-1]*W for i in range(H)]
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
for i in range(H):
  for j in range(W):
    if A[i][j] == '#':
      dist[i][j] = 0
      que.append((i, j))

d = 0
while que:
  y, x = que.popleft()
  d = dist[y][x]
  for dx, dy in dd:
    nx = x + dx; ny = y + dy
    if not 0 <= nx < W or not 0 <= ny < H or dist[ny][nx] != -1:
      continue
    dist[ny][nx] = d + 1
    que.append((ny, nx))

print(d)