C_grid = [list(map(int, input().split())) for i in range(3)]
a1, a2, a3 = C_grid[0][1] - C_grid[0][0], C_grid[0][2] - C_grid[0][1], C_grid[0][0] - C_grid[0][2]
for i in range(1, 3):
    gyo = C_grid[i]
    k1, k2, k3 = gyo[1] - gyo[0], gyo[2] - gyo[1], gyo[0] - gyo[2]
    if a1 == k1 and a2 == k2 and a3 == k3:
        continue
    else:
        print('No')
        exit(0)

a1, a2, a3 = C_grid[1][0] - C_grid[0][0], C_grid[2][0] - C_grid[1][0], C_grid[0][0] - C_grid[2][0]
for i in range(1, 3):
    k1, k2, k3 = C_grid[1][i] - C_grid[0][i], C_grid[2][i] - C_grid[1][i], C_grid[0][i] - C_grid[2][i]
    if a1 == k1 and a2 == k2 and a3 == k3:
        continue
    else:
        print('No')
        exit(0)
print('Yes')
