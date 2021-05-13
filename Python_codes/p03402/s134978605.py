A, B = map(int, input().split())

K = 50
a = '.'
b = '#'
grid = [[a] * (2 * K) for _ in range(K)] + [[b] * (2 * K) for _ in range(K)]

B -= 1
for i in range(1, K - 1, 2):
    for j in range(1, 2 * K - 1):
        if (i + j) % 2:
            grid[i][j] = b
            B -= 1
        if B == 0:
            break
    else:
        continue
    break

A -= 1
for i in range(K + 1, 2 * K - 1, 2):
    for j in range(1, 2 * K - 1):
        if (i + j) % 2:
            grid[i][j] = a
            A -= 1
        if A == 0:
            break
    else:
        continue
    break

print(2 * K, 2 * K)
for r in grid:
    print(*r, sep='')
