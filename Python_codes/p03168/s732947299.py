N = int(input())
A = list(map(float, input().split()))

# コインをi枚使い、表がj枚である確率
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(i+1):
        if j-1 >= 0:
            dp[i][j] = dp[i-1][j-1]*A[i-1] + dp[i-1][j]*(1 - A[i-1])
        else:
            dp[i][j] = dp[i-1][j]*(1 - A[i-1])

print(sum([dp[N][i] for i in range(N//2+1, N+1)]))