N, M, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]
Y = [list(map(int, input().split())) for _ in range(Q)]

grid = [[0] * (N + 1) for _ in range(N + 1)]
for l, r in X:
    grid[l][r] += 1

for i in range(N):
    for j in range(N):
        grid[i + 1][j + 1] += grid[i][j + 1]

for i in range(N):
    for j in range(N):
        grid[i + 1][j + 1] += grid[i + 1][j]

for p, q in Y:
    print(grid[q][q] + grid[p - 1][p - 1] - grid[p - 1][q] - grid[q][p - 1])
