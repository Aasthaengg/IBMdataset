A, B = map(int, input().split())
grid = [['#'] * 100 for _ in range(20)] + [['.'] * 100 for _ in range(20)]
A -= 1
cnt = 0
i = 0
j = 0
while cnt < A:
    grid[i][j] = '.'
    cnt += 1
    j += 2
    if j >= 100:
        i += 2
        j = 0
B -= 1
cnt = 0
i = 39
j = 0
while cnt < B:
    grid[i][j] = '#'
    cnt += 1
    j += 2
    if j >= 100:
        i -= 2
        j = 0
print(40, 100)
for row in grid:
    print(''.join(row))
