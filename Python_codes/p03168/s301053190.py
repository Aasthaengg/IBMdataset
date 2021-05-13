N = int(input())
P = list(map(float, input().split()))

"""
dp[i][j]: i枚投げた時にj枚表の確率
"""
dp = [[0] * (N+1) for _ in range(N+1)]
dp[1][0] = 1 - P[0]
dp[1][1] = P[0]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] += dp[i-1][j-1] * P[i-1]
        dp[i][j-1] += dp[i-1][j-1] * (1-P[i-1])

ans = 0
for i in range(N+1):
    if N//2 < i:
        ans += dp[N][i]
print(ans)
