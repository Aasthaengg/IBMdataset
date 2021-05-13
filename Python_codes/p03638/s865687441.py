H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

grid = [[0] * W for _ in range(H)]

i, j, k = 0, 0, 0
while i < H:
    step = 1 if i % 2 == 0 else -1
    grid[i][j] = k + 1
    A[k] -= 1
    if A[k] == 0:
        k += 1
    if j + step in (-1, W):
        i += 1
    else:
        j += step

for row in grid:
    print(*row)
