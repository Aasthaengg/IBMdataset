h, w = list(map(int, input().split()))

grid = []

for i in range(h):
    row = list(input()) 

    for i in range(len(row)):
        if row[i] == '.':
            row[i] = 0
    
    grid.append(row)

num = 1000000007

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            continue
        if i == 0 and j == 0:
            grid[i][j] = 1
        elif i == 0:
            if grid[i][j-1] != '#':
                grid[i][j] = grid[i][j-1] % num
        elif j == 0:
            if grid[i-1][j] != '#':
                grid[i][j] = grid[i-1][j] % num
        else:
            if grid[i][j-1] == '#' and grid[i-1][j] == '#':
                grid[i][j] = 0
            elif grid[i][j-1] == '#':
                grid[i][j] = grid[i-1][j] % num
            elif grid[i-1][j] == '#':
                grid[i][j] = grid[i][j-1] % num
            else:
                grid[i][j] = (grid[i-1][j] + grid[i][j-1]) % num

print(grid[-1][-1])