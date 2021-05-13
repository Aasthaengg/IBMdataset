H, W = map(int, input().split())
X = [input() for _ in range(H)]

grid0 = [[0] * (W + 1) for _ in range(H + 1)]

# L -> R
for i in range(H):
    for j in range(W):
        if X[i][j] == ".":
            grid0[i + 1][j + 1] = grid0[i + 1][j] + 1
        
# L <- R
for i in range(H):
    for j in reversed(range(W)):
        if grid0[i + 1][j] > 0:
            grid0[i + 1][j] = max(grid0[i + 1][j], grid0[i + 1][j + 1])

grid1 = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        if X[i][j] == ".":
            grid1[i + 1][j + 1] = grid1[i][j + 1] + 1

for i in reversed(range(H)):
    for j in range(W):
        if grid1[i][j + 1] > 0:
            grid1[i][j + 1] = max(grid1[i][j + 1], grid1[i + 1][j + 1])

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, grid0[i + 1][j + 1] + grid1[i + 1][j + 1] - 1)
print(ans)
