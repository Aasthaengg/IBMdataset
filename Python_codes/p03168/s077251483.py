N = int(input())
inp = list(map(lambda x: float(x), input().split(" ")))

dp = [[0]*(N+1) for i in range(N+1)]
dp[0][0] = 1.0

for i in range(N):
    for j in range(i+1):
        dp[i+1][j] += dp[i][j]*(1-inp[i])
        dp[i+1][j+1] += dp[i][j]*inp[i]

print(sum(dp[N][(N//2+1):N+1]))