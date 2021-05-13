N = int(input())

dp = [10**100]*(N + 10**6)
dp[0] = 0
delta = [1, 6, 6**2, 6**3, 6**4, 6**5, 6**6, 9, 9**2, 9**3, 9**4, 9**5]
for i in range(0, N):
    for d in delta:
        dp[i+d] = min(dp[i+d], dp[i] + 1)
print(dp[N])