MOD = int(1e9 + 7)

sizeI, sizeJ, targetJ = map(int, input().split())

validRows = [row for row in range(1 << (sizeJ - 1)) if '11' not in bin(row)]
# dp[i][j] - number of ways to come to position (i, j)
dp = [[0 for _ in range(sizeJ)] for _ in range(sizeI + 1)]
dp[0][0] = 1
for i in range(1, sizeI + 1):
    for j in range(sizeJ):
        for prevRow in validRows:
            if j - 1 >= 0 and (prevRow >> (j - 1)) & 1:
                dp[i][j] += dp[i - 1][j - 1]
            elif (prevRow >> j) & 1:
                dp[i][j] += dp[i - 1][j + 1]
            else:
                dp[i][j] += dp[i - 1][j]
            dp[i][j] %= MOD
print(dp[sizeI][targetJ - 1])