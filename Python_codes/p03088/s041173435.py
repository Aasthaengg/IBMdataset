n = int(input())
MOD = 10**9 + 7
# dp[i][x][y][z] 0:A 1:C 2:G 3:T
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
dp[0][3][3][3] = 1
for i in range(1, n+1):
    for x in range(4):
        for y in range(4):
            for z in range(4):
                for w in range(4):
                    if x == 0 and z == 2 and w == 1:
                        continue
                    elif y == 0 and z == 2 and w == 1:
                        continue
                    elif y == 2 and z == 0 and w == 1:
                        continue
                    elif y == 0 and z == 1 and w == 2:
                        continue
                    elif x == 0 and y == 2 and w == 1:
                        continue

                    dp[i][y][z][w] += dp[i-1][x][y][z]
                    dp[i][y][z][w] %= MOD

ans = 0
for x in range(4):
    for y in range(4):
        for z in range(4):
            ans += dp[n][x][y][z]
            ans %= MOD

print(ans)