A, B = map(int, input().split())
print(100, 100)
grid = [['#'] * 100 for _ in range(50)] + [['.'] * 100 for _ in range(50)]
A -= 1; B -= 1
i, j = 0, 0
while A:
    grid[i][j] = '.'; A -= 1
    if j == 98: i += 2; j = 0
    else: j += 2
i, j = 51, 0
while B:
    grid[i][j] = '#'; B -= 1
    if j == 98: i += 2; j = 0
    else: j += 2
for r in grid:
    print(''.join(r))