N = int(input())
P = list(map(float, input().split()))
P = [0] + P
dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    dp[i][0] = dp[i-1][0] * (1 - P[i])

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i][j] += dp[i-1][j-1] * P[i] + dp[i-1][j] * (1 - P[i]) 

ans = 0
if N % 2 == 0:
    start = N // 2
else:
    start = N // 2 + 1

for i in range(start, N+1):
    ans += dp[N][i]
    
print(ans)