# -*- coding: utf-8 -*-
# 17:46 -> 

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

H, W = map(int, input().split())

grid = []
num_shiro = 0
for i in range(H):
    grid.append(list(input()))
    num_shiro += sum([dot == '.' for dot in grid[i]])

# 最も近道させ、残りに黒マスを塗るのがよき.
# 幅優先探索
grid_queue = deque()
grid_queue.append((0,0))
grid[0][0] = 1

while len(grid_queue) != 0:
    x, y = grid_queue.popleft()
    depth = grid[x][y]
    for k in range(4):
        new_x = x+dx[k]
        new_y = y+dy[k]
        if 0 <= new_x < H and 0 <= new_y < W and \
            grid[new_x][new_y] == '.':
            if (new_x, new_y) == (H-1, W-1):
                print(num_shiro-depth-1)
                exit(0)
            else:
                grid_queue.append((new_x, new_y))
                grid[new_x][new_y] = depth+1

if grid[H-1][W-1] == '.':
    print(-1)
else:
    print(num_shiro-grid[H-1][W-1])