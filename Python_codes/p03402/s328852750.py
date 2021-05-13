import numpy as np
a,b = map(int, input().split())
grid1 = [['.' for j in range(100)] for i in range(50)]
grid2 = [['#' for j in range(100)] for i in range(50)]
a -= 1
b -= 1
x = y = 1

for i in range(a):
    grid2[x][y] = '.'
    y += 2
    if y != y % 100:
        x += 2
    y = y % 100
    if x >= 50 or y >= 100:break

x = y = 1
for i in range(b):
    grid1[x][y] = '#'
    y += 2
    if y != y % 100:
        x += 2
    y = y % 100
    if x >= 50 or y >= 100:break

print(100, 100)
grid = np.concatenate((grid1, grid2), axis=0)
for row in grid:
    print(''.join(row))