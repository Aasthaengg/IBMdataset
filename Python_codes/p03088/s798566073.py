import sys
input = sys.stdin.readline

mod = 10**9 + 7
n = int(input())

dp = [[[[1]*4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]

dp[3][0][1][2] = 0
dp[3][1][0][2] = 0
dp[3][0][2][1] = 0

if n == 3:
    ans = 0
    for i in dp[-1]:
        for j in i:
            for k in j:
                ans += k
    print(ans)
    sys.exit()

for i in range(4, n + 1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if (j == 0 and k == 1 and l == 2) or (j == 1 and k == 0 and l == 2) or (j == 0 and k == 2 and l == 1):
                    dp[i][j][k][l] = 0
                    continue
                if l != 2:
                    dp[i][j][k][l] = sum([dp[i - 1][x][j][k] for x in range(4)])
                    dp[i][j][k][l] %= mod
                    continue
                dp[i][j][k][l] = sum([dp[i - 1][x][j][k] for x in range(4)])
                dp[i][j][k][l] %= mod

                if l == 2 and k == 1:
                    dp[i][j][k][l] -= dp[i - 1][0][j][1]
                    dp[i][j][k][l] %= mod
                
                if l == 2 and j == 1:
                    dp[i][j][k][l] -= dp[i - 1][0][1][k]
                    dp[i][j][k][l] %= mod
                
                if l == 2 and j == 1 and k == 1:
                    dp[i][j][k][l] += dp[i - 1][0][1][1]
                    dp[i][j][k][l] %= mod


ans = 0
for i in dp[-1]:
    for j in i:
        for k in j:
            ans += k
            ans %= mod
print(ans)
