N = int(input())
P = list(map(float, input().split()))

dp = [[0 for _ in  range(N+1)] for _ in range(N+1)] # dp[i][j]: コインをi+1枚投げたとき、表がj枚出る確率

dp[0][0] = 1

for i in range(N):
    for j in range(0, i+1):
        dp[i+1][j] += dp[i][j] * (1 - P[i])
        dp[i+1][j+1] += dp[i][j] * P[i]

ans = 0
for i in range(N+1)[::-1]:
    if i > (N - i):        
        ans += dp[N][i]

print(ans)