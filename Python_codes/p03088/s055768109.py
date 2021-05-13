import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]

dp[0][3][3][3] = 1

MOD = 10 ** 9 + 7
for l in range(N):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if dp[l][i][j][k] == 0:
                    continue
                
                for n in range(4):
                    if j == 0 and k == 2 and n == 1: continue
                    if j == 0 and k == 1 and n == 2: continue
                    if j == 1 and k == 0 and n == 2: continue

                    if i == 0 and j == 1 and n == 2: continue
                    if i == 0 and k == 1 and n == 2: continue 

                    dp[l+1][j][k][n] += dp[l][i][j][k]
                    dp[l+1][j][k][n] %= MOD
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]
            ans %= MOD
print(ans%MOD)