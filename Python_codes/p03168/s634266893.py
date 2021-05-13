N = int(input())
p = list(map(float, input().split()))
dp = [0] * (N+1) # the probability of getting j heads
dp[0] = 1
for i in range(N):
    ndp = [0] * (N+1)
    ndp[0] = dp[0] * (1 - p[i])
    for j in range(1, N+1):
        ndp[j] = dp[j-1] * p[i] + dp[j] * (1 - p[i])
    dp = ndp
print(sum(dp[N//2+1:]))