import numpy as np

A, B = map(int, input().split())

K = 50
grid = np.ones((100, 100), dtype='int')

# 白1黒0
grid[:K, :] = 0

A -= 1
col = 0
row = 0
while A:
    if A >= K:
        grid[col, ::2] = 1
        A -= K
        col += 2
        continue

    grid[col, row] = 1
    row += 2
    A -= 1

B -= 1
col = K + 1
row = 0
while B:
    if B >= K:
        grid[col, ::2] = 0
        B -= K
        col += 2
        continue

    grid[col, row] = 0
    row += 2
    B -= 1

grid = np.where(grid, '.', '#')
print(100, 100)
print('\n'.join(map(''.join, grid.tolist())))