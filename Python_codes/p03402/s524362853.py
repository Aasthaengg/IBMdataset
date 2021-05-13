a, b = map(int, input().split())
a -= 1
b -= 1
size = 100
grid = [[['.'], ['#']][h >= size//2] * size for h in range(size)]
for i in range(a):
    grid[size - 1 - (i // (size//2)) * 2][size - 1 - (i % (size//2)) * 2] = '.'
for i in range(b):
    grid[(i // (size//2)) * 2][(i % (size//2)) * 2] = '#'
print(size, size)
for i in range(size):
    for j in range(size):
        print(grid[i][j], end = '')
    print()
