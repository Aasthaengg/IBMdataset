A, B = map(int, input().split())

WHITE = '.'
BLACK = '#'

K = 50

grid = [[BLACK for _ in range(2*K)] for _ in range(2*K)]
for y in range(K, 2*K):
    for x in range(2*K):
        grid[y][x] = WHITE

A -= 1
B -= 1

for y in range(0, K-1, 2):
    for i in range(K):
        if A > 0:
            grid[y][2*i] = WHITE
            A -= 1
        else:
            break

for y in range(0, K-1, 2):
    for i in range(K):
        if B > 0:
            grid[y+K+1][2*i] = BLACK
            B -= 1
        else:
            break

print("{0} {1}".format(2*K, 2*K))
for g in grid:
    print("".join(g))
