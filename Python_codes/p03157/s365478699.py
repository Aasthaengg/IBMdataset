h, w = map(int, input().split())
S = [[1 if i=="#" else 0 for i in input()] for _ in range(h)]
dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)
seen = [[False]*w for _ in range(h)]

def dfs(y, x):
  white = 0
  black = 0
  stack = [(y, x)]
  seen[y][x] = True
  while stack:
    s, t = stack.pop()
    if S[s][t]:
      black += 1
    else:
      white += 1
    for di, dj in zip(dy, dx):
      ny, nx = s+di, t+dj
      if 0 <= ny < h and 0 <= nx < w:
        if seen[ny][nx]:
          continue
        if S[s][t] ^ S[ny][nx]:
          seen[ny][nx] = True
          stack.append((ny, nx))
  return black, white

ans = 0
for i in range(h):
  for j in range(w):
    if not seen[i][j]:
      black, white = dfs(i, j)
      ans += black * white
print(ans)