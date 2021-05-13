from collections import deque
H,W=map(int,input().split())
grid = [input() for i in range(H)]

dist = [[-1]*W for _ in range(H)]
black_cells = deque()
#黒マスの位置をblack_cellsに保持
#distの黒マスの部分に0でフラッグ
for h in range(H):
  for w in range(W):
    if grid[h][w]=="#":
      black_cells.append((h,w))
      dist[h][w] = 0
def bfs(black_cells, dist):
  count=0
  while black_cells:
    h,w = black_cells.popleft()
    count = dist[h][w]
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        new_h = h + dy
        new_w = w + dx
        if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
          continue
        if dist[new_h][new_w] == -1:
          dist[new_h][new_w] = count+1
          black_cells.append((new_h,new_w))
  return count
print(bfs(black_cells,dist))