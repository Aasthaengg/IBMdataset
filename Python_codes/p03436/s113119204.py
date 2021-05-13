from collections import deque
H,W = map(int,input().split())
grid = [0] * H
num_black = 0
for i in range(H):
    s = input()
    for j in range(len(s)):
        if s[j] == '#':
            num_black += 1
    grid[i] = list(s)
time_grid = [[-1] * W for _ in range(H)]
time_grid[0][0] = 0
queue = deque()
queue.append([0,0,0])
while queue:
    y,x,t = queue.popleft()
    for next_y, next_x in [[y+1,x],[y,x+1],[y-1,x],[y,x-1]]:
        if 0 <= next_x < W and 0 <= next_y < H and grid[next_y][next_x] == '.':
            queue.append([next_y,next_x,t+1])
            time_grid[next_y][next_x] = t+1
            grid[next_y][next_x] = '#'
if time_grid[H-1][W-1] != -1:
    print(H*W-time_grid[-1][-1]-1-num_black)
else:
    print(-1)


