from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
dist = [[-1]*w for _ in range(h)]  # 黒ならdist[i][j]は0、白なら-1

black_cells = deque()

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            black_cells.append((i, j))
            dist[i][j] = 0

def bfs(black_cells, dist):
    d = 0
    while black_cells:
        h_black, w_black = black_cells.popleft()
        d=dist[h_black][w_black]
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_h = h_black+dy
            new_w = w_black+dx
            if new_h < 0 or h <= new_h or new_w < 0 or w <= new_w:
                continue
            if dist[new_h][new_w] == -1:
                dist[new_h][new_w] = d+1
                black_cells.append((new_h, new_w))
    return d

d = bfs(black_cells, dist)
print(d)
