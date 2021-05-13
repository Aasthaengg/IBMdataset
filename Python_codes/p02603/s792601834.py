
N = int(input())
A = list(map(int, input().split()))


dp = [0] * 100
dp[0] = 1000
for i in range(1,N):
    dp[i] = dp[i-1]
    for j in range(0,i):
        V = int(dp[j] / A[j])
        W = dp[j] + (A[i] - A[j]) * V
        dp[i] = max(dp[i], W)
print(dp[N-1])

