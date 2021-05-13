N = int(input())
*A, = map(int, input().split())

dp = [0]*(N+1)
dp[0] = 1000

for i in range(1, N+1):
    dp[i] = dp[i-1]
    for j in range(1, i):
        dp[i] = max(dp[i], (dp[j]//A[j-1])*A[i-1] + (dp[j]%A[j-1]))

print(dp[-1])
