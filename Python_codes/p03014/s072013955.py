H,W = map(int,input().split())
grid = [0] * H
for i in range(H):
    grid[i] = input()
right = [[0]*W for _ in range(H)]
left = [[0]*W for _ in range(H)]
up = [[0]*W for _ in range(H)]
down = [[0]*W for _ in range(H)]
for i in range(H):
    now = 0
    for x in range(W):
        if grid[i][x] == '.':
            left[i][x] = now
            now += 1
        else:
            now = 0
    now = 0
    for x in range(W-1,-1,-1):
        if grid[i][x] == '.':
            right[i][x] = now
            now += 1
        else:
            now = 0
for x in range(W):
    now = 0
    for y in range(H):
        if grid[y][x] == '.':
            up[y][x] = now
            now += 1
        else:
            now = 0
    now = 0
    for y in range(H-1,-1,-1):
        if grid[y][x] == '.':
            down[y][x] = now
            now += 1
        else:
            now = 0
ans = 0
for y in range(H):
    for x in range(W):
        if grid[y][x] == '.':
            can = 1 + right[y][x] + left[y][x] + up[y][x] + down[y][x]
            ans = max(ans,can)
print(ans)
