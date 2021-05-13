h, w = map(int, input().split())
mat = [input() for _ in range(h)]

dp = [[0]*w for _ in range(h)]
if mat[0][0] == "#":
    dp[0][0] = 1
for i in range(1, w):
    if mat[0][i] != mat[0][i-1] and mat[0][i] == "#":
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1]
for j in range(1, h):
    if mat[j][0] != mat[j-1][0] and mat[j][0] == "#":
        dp[j][0] = dp[j-1][0] + 1
    else:
        dp[j][0] = dp[j-1][0]

for i in range(1, h):
    for j in range(1, w):
        ver = dp[i-1][j]
        hor = dp[i][j-1]
        if mat[i-1][j] != mat[i][j] and mat[i][j] == "#":
            ver += 1
        if mat[i][j-1] != mat[i][j] and mat[i][j] == "#":
            hor += 1
        dp[i][j] = min(ver, hor)
print(dp[h-1][w-1])
