N, P = map(int,input().split())
A = list(map(int,input().split()))
dp = [[0,0] for k in range(N+1)]
dp[0][0] = 1
for k in range(N):
    if A[k]%2 == 0:
        dp[k+1][0] = dp[k][0]*2
        dp[k+1][1] = dp[k][1]*2
    else:
        dp[k+1][0] = dp[k][0] + dp[k][1]
        dp[k+1][1] = dp[k][1] + dp[k][0]

print(dp[N][P])
