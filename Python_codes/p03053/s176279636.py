import sys 
from collections import deque
 
h, w = map(int, sys.stdin.readline().split())
grid = []
for _ in range(h):
    grid.append(list(sys.stdin.readline().strip()))
 
q = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            q.append((0, i, j))
 
while q:
    count, y, x = q.popleft()
    for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        if 0 <= y+dy < h and 0 <= x+dx < w:
            if grid[y+dy][x+dx] == "#":
                continue
            else:
                grid[y+dy][x+dx] = "#"
                q.append((count+1, y+dy, x+dx))
 
print(count)