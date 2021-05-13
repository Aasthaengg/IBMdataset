h, w = map(int, input().split())
grid = ['#' * (h + 2)]
for _ in range(h):
    grid.append('#' + input() + '#')
grid.append('#' * (h + 2))
lgrid = [[0 for _ in range(w+2)] for _ in range(h+2)]
rgrid = [[0 for _ in range(w+2)] for _ in range(h+2)]
dgrid = [[0 for _ in range(w+2)] for _ in range(h+2)]
ugrid = [[0 for _ in range(w+2)] for _ in range(h+2)]
for i in range(1, h+1):
    for j in range(1, w+1):
        if grid[i][j] == '#':
            lgrid[i][j] = 0
            ugrid[i][j] = 0
        else:
            lgrid[i][j] = lgrid[i][j-1] + 1
            ugrid[i][j] = ugrid[i-1][j] + 1
        if grid[i][w+1-j] == '#':
            rgrid[i][w+1-j] = 0
        else:
            rgrid[i][w+1-j] = rgrid[i][w+2-j] + 1
        if grid[h+1-i][j] == '#':
            dgrid[h+1-i][j] = 0
        else:
            dgrid[h+1-i][j] = dgrid[h+2-i][j] + 1        
cnt = 0
for i in range(1, h+1):
    for j in range(1, w+1):
        tmp = lgrid[i][j]+rgrid[i][j]+ugrid[i][j]+dgrid[i][j] - 3
        cnt = max(cnt, tmp)
print(cnt)
