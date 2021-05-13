N = int(input())
M = 10**9 + 7

dp = [
    [[[1 if i==0 else 0 for i in range(N-2)] for j in range(4)]
    for k in range(4)] for j in range(4)
    ]

dp[0][1][2][0] = 0
dp[0][2][1][0] = 0
dp[1][0][2][0] = 0

for m in range(N-3):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    dp[j][k][l][m+1] += dp[i][j][k][m]
                    dp[j][k][l][m+1] %= M
                    dp[0][1][2][m+1] = 0
                    dp[0][2][1][m+1] = 0
                    dp[1][0][2][m+1] = 0

                    if (i==0):
                        for o in range(4):
                            dp[o][1][2][m+1] = 0
                            dp[1][o][2][m+1] = 0

total = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            total += dp[i][j][k][N-3]
            total %= M
print(total)