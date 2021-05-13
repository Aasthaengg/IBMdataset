n, ma, mb = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(n)]

m = n * 10 + 1

dp = [[[float('inf')] * m for j in range(m)] for i in range(n + 1)]
for i in range(n + 1):
    dp[i][0][0] = 0

for i in range(n):
    for j in range(m):
        for k in range(m):
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

            # i個目を買う
            jj = j + abc[i][0]
            kk = k + abc[i][1]
            if jj < m and kk < m:
                dp[i+1][jj][kk] = min(dp[i+1][jj][kk], dp[i][j][k] + abc[i][2])

from fractions import gcd
ans = float('inf')
for i in range(1, m):
    for j in range(1, m):
        g = gcd(i, j)
        if i // g == ma and j // g == mb:
            ans = min(ans, dp[-1][i][j])

if ans == float('inf'):
    print(-1)
else:
    print(ans)
