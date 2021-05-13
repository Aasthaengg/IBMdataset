a, b = map(int, input().split())

grid = []
for i in range(50):
    line = ['#'] * 100
    grid.append(line)

for i in range(50):
    line = ['.'] * 100
    grid.append(line)

count = 0
for y in range(0, 50, 2):
    for x in range(0, 100, 2):
        if count == a - 1:
            break
        grid[y][x] = '.'
        count += 1
    if count == a - 1:
        break

count = 0
for y in range(51, 100, 2):
    for x in range(0, 100, 2):
        if count == b-1:
            break
        grid[y][x] = '#'
        count += 1
    if count == b - 1:
        break

print(100, 100)
for line in grid:
    print(''.join(line))