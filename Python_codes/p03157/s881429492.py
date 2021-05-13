import sys
sys.setrecursionlimit(10**9)

H, W = map(int, input().split())
S = [input() for i in range(H)]

visited = set()
def dfs(x, y, c, white, black):
  global visited
  for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    xx = x + dx; yy = y + dy
    if 0<=xx<H and 0<=yy<W and (xx, yy) not in visited and S[xx][yy]!=c:
      cc = S[xx][yy]
      if cc == '.':
        white.add((xx, yy))
      else:
        black.add((xx, yy))
      visited.add((xx, yy))
      white, black = dfs(xx, yy, cc, white, black)
  return white, black

ans = 0
for x in range(H):
  for y in range(W):
    if (x, y) not in visited:
      visited.add((x, y))
      c = S[x][y]
      if c == '.':
        white = set(((x, y), )); black = set()
      else:
        white = set(); black = set(((x, y), ))
      white, black = dfs(x, y, c, white, black)
      ans += len(white) * len(black)

print(ans)