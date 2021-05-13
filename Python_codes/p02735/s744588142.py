h,w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
dpgrid = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        d = 1 if grid[i][j] == "#" else 0
        if (i == 0) & (j == 0):
            dpgrid[i][j] = d
        elif (i == 0):
            a = 1 if (grid[i][j-1] == ".") & (d == 1) else 0
            dpgrid[i][j] = a + dpgrid[i][j-1]
        elif (j == 0):
            b = 1 if (grid[i-1][j] == ".") & (d == 1) else 0
            dpgrid[i][j] = b + dpgrid[i-1][j]
        else:
            a = 1 if (grid[i][j-1] == ".") & (d == 1) else 0
            b = 1 if (grid[i-1][j] == ".") & (d == 1) else 0
            dpgrid[i][j] = min(a + dpgrid[i][j-1], b + dpgrid[i-1][j])
print(dpgrid[h-1][w-1])