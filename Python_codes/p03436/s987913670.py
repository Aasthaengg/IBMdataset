import sys
from collections import deque
import numpy as np

h, w = map(int, input().split())

grid = [list(map(str, input().rstrip())) for _ in range(h)]
init = np.where(np.array(grid).flatten() == "#")[0].shape[0]

moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

q = deque([[0, 0]])
grid[0][0] = 1

while q:
    curr = q.popleft()
    for m in moves:
        nx = curr[0] + m[0]
        ny = curr[1] + m[1]
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == ".":
                grid[nx][ny] = grid[curr[0]][curr[1]] + 1
                q.append([nx, ny])
                if nx == h - 1 and ny == w - 1:
                    print(h * w - grid[nx][ny] - init)
                    sys.exit()
else:
    print(-1)