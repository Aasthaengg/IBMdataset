grid = []
for i in range(3):
    grid.append(list(map(int, input().split())))
b = grid[0]
a = (0, grid[1][1]-b[1], grid[2][2]-b[2])

for i in range(3):
    for j in range(3):
        if a[i]+b[j] != grid[i][j]:
            print('No')
            exit(0)

print('Yes')
