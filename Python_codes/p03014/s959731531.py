h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
up = [[0 for i in range(w)] for j in range(h)]
down = [[0 for i in range(w)] for j in range(h)]
right = [[0 for i in range(w)] for j in range(h)]
left = [[0 for i in range(w)] for j in range(h)]
for i in range(w):
    # init up
    if grid[0][i] == ".":
        up[0][i] = 1
    else:
        up[0][i] = 0
    #init down
    if grid[-1][i] == ".":
        down[-1][i] = 1
    else:
        down[-1][i] = 0
for i in range(h):
    #init right
    if grid[i][-1] == ".":
        right[i][-1] = 1
    else:
        right[i][-1] = 0
    
    #init left
    if grid[i][0] == ".":
        left[i][0] = 1
    else:
        left[i][0] = 0
for i in range(h):
    for j in range(1,w):
        if grid[i][j] == ".":
            left[i][j] = left[i][j-1] + 1
        else:
            left[i][j] = 0
for i in range(h):
    for j in range(w-2,-1,-1):
        if grid[i][j] == ".":
            right[i][j] = right[i][j+1] + 1
        else:
            right[i][j] = 0

for i in range(1,h):
    for j in range(w):
        if grid[i][j] == ".":
            up[i][j] = up[i-1][j] + 1
        else:
            up[i][j] = 0
for i in range(h-2,-1,-1):
    for j in range(w):
        if grid[i][j] == ".":
            down[i][j] = down[i+1][j] + 1
        else:
            down[i][j] = 0
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, up[i][j] + down[i][j] + left[i][j] + right[i][j] - 3)
print(ans)