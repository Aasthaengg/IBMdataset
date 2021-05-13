h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))

GRID = [[0] * w for _ in range(h)]

PATH = []
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            PATH.append((i, j))
    else:
        for j in range(w)[::-1]:
            PATH.append((i, j))

color = 1
count = 0
for i, j in PATH:
    GRID[i][j] = color
    count += 1
    if count == A[color - 1]:
        color += 1
        count = 0

for ROW in GRID:
    print(*ROW)
