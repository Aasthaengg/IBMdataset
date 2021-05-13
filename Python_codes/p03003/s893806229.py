N,M = map(int, input().split())
S = [int(s) for s in input().split()]
T = [int(t) for t in input().split()]

mod = 10**9+7
dp = [[0]*(M+1) for _ in range(N+1)]
sum2D = [[0]*(M+1) for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, M+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = sum2D[i-1][j-1] + 1
            dp[i][j] %= mod
        sum2D[i][j] = dp[i][j] + sum2D[i-1][j] + sum2D[i][j-1] - sum2D[i-1][j-1]
        sum2D[i][j] %= mod
        
ans = 1
for i in range(1, N+1):
    for j in range(1, M+1):
        ans += dp[i][j]
        ans %= mod
        
print(ans)