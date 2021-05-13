# "#"と"."だけで行き来できるエリアを"島"とする
# 島にある"#"から"."には必ず行けるので、
# "#"の数 * "."がその島の場合の数。これをすべて足し合わせる

# visitedになっていない点をすべて捜査する。
# 進めなかった（"#"もしくは"."が連続した）マスはvisitedにしない。

H,W = map(int,input().split())
grid = [None] * H
for i in range(H):
  grid[i] = input()
  
visited = [[False] * W for i in range(H)]

def get_next_unvisited(checked_y):
  for i in range(checked_y,H):
    for j in range(W):
      if not visited[i][j]:
        return i,j
  return -1,-1 # 候補なし
  
from collections import deque
ans = 0
cases = ((0,1),(0,-1),(1,0),(-1,0))
checked_y = 0
while True:
  y,x = get_next_unvisited(checked_y)
  if y == -1 and x == -1:
    print(ans)
    exit(0)
  checked_y = y
  # y,x,親,親マスの文字
  q = deque([[y,x,-1,-1,"N"]])
  black = 0
  white = 0
  
  while q:
    y,x,parent_y,parent_x,parent = q.pop()
    if visited[y][x]:
      continue
    point = grid[y][x]
    if point == parent:
      continue
    visited[y][x] = True
    if point == "#":
      black += 1
    if point == ".":
      white += 1
    for c in cases:
      if y + c[0] == parent_y and x + c[1] == parent_x:
        continue
      if 0 <= y + c[0] < H and 0 <= x + c[1] < W:
        q.append([y + c[0],x + c[1],y,x, point])
  ans += black * white
