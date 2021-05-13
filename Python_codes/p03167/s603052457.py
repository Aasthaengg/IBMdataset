r, c = map(int, input().split())
mat = [input() for _ in range(r)]
dp = [[0]*c for _ in range(r)]
for i in range(c):
    if mat[0][i] == '#':
        break
    dp[0][i] = 1
for i in range(r):
    if mat[i][0] == '#':
        break
    dp[i][0] = 1
for i in range(1, r):
    for j in range(1, c):
        if mat[i][j] != '#':
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % (10**9 + 7)
print(dp[-1][-1])