from collections import deque
H,W = map(int,input().split())
grid = []
d = deque()
next_d = deque()
for i in range(H):
    grid.append(list(input()))
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            d.append((i,j))
dx = [0,-1,0,1]
dy = [1,0,-1,0]
ans = -1
while d:
    ans += 1
    while d:
        y,x = d.pop()
        for i in range(4):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if next_y >= 0 and next_y < H and next_x >= 0 and next_x < W:
                if grid[next_y][next_x] == '.':
                    grid[next_y][next_x] = '#'
                    next_d.append((next_y,next_x))
    d = next_d
    next_d = deque()
print(ans)