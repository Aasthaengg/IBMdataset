H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

ans = [[0] * W for _ in range(H)]

if grid[0][0] == "#":
    ans[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue

        r = H*W
        d = H*W
        if j > 0 and grid[i][j] != grid[i][j-1] and grid[i][j-1] == ".":
            r = 1 + ans[i][j-1]
        elif j > 0:
            r = ans[i][j-1]

        if i > 0 and grid[i][j] != grid[i-1][j] and grid[i-1][j] == ".":
            d = 1 + ans[i-1][j]
        elif i > 0:
            d = ans[i-1][j]
        ans[i][j] = min(r, d)

print(ans[H-1][W-1])