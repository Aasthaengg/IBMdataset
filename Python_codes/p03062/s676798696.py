N = int(input())
A = list(map(int,input().split()))

INF = float('inf')
dp = [[-INF]*2 for _ in range(N+1)]
dp[0][0] = 0
for i,a in enumerate(A):
    dp[i+1][0] = max(dp[i+1][0], dp[i][0]+a, dp[i][1]-a)
    dp[i+1][1] = max(dp[i+1][1], dp[i][0]-a, dp[i][1]+a)
print(dp[-1][0])