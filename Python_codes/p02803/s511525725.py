from collections import deque
import copy
H,W = map(int,input().split())
grid = [[0]*W for _ in range(H)]
for i in range(H):
    grid[i] = list(input())
ans = 0
for sy in range(H):
    for sx in range(W):
        if grid[sy][sx] == '#':
            continue
        now_grid = copy.deepcopy(grid)
        time_grid = [[-1]*W for _ in range(H)]
        queue = deque()
        queue.append([sy,sx,0])
        now_grid[sy][sx] = '#'
        while queue:
            y,x,t = queue.popleft()
            for next_y, next_x in [[y+1, x],[y,x+1],[y-1,x],[y,x-1]]:
                if 0<= next_y < H and 0 <= next_x < W and now_grid[next_y][next_x] != '#':
                    queue.append([next_y,next_x,t+1])
                    time_grid[next_y][next_x] = t+1
                    now_grid[next_y][next_x] = '#'
        Max= 0
        for i in range(H):
            for j in range(W):
                Max = max(Max,time_grid[i][j])
        ans = max(ans, Max)
print(ans)

