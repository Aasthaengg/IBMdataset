h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]
left = [[0] * w for _ in range(h)]
right = [[0] * w for _ in range(h)]
up = [[0] * w for _ in range(h)]
down = [[0] * w for _ in range(h)]

for i in range(h):
    current = 0
    for j in range(w):
        if grid[i][j] == '#':
            current = 0
        else:
            current += 1
        left[i][j] = current
    
for i in range(h):
    current = 0
    for j in range(w - 1, -1, -1):
        if grid[i][j] == '#':
            current = 0
        else:
            current += 1
        right[i][j] = current

for i in range(w):
    current = 0
    for j in range(h):
        if grid[j][i] == '#':
            current = 0
        else:
            current += 1
        up[j][i] = current

for i in range(w):
    current = 0
    for j in range(h - 1, -1, -1):
        if grid[j][i] == '#':
            current = 0
        else:
            current += 1
        down[j][i] = current

ans = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            continue
        ans = max(ans, left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3)

print(ans)