MOD = 10**9+7
n = int(input())

dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
dp[0][0][0][0] = 1

for i in range(n):
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                for nxt in range(4):
                    if nxt == 3 and c1 == 2 and c2 == 1: continue
                    if nxt == 2 and c1 == 3 and c2 == 1: continue
                    if nxt == 3 and c1 == 1 and c2 == 2: continue
                    if nxt == 3 and c2 == 2 and c3 == 1: continue
                    if nxt == 3 and c1 == 2 and c3 == 1: continue
                    dp[i+1][nxt][c1][c2] += dp[i][c1][c2][c3]
                    dp[i+1][nxt][c1][c2] %= MOD

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n][i][j][k]
            ans %= MOD

print(ans)
