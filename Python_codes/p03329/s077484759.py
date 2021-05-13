N = int(input())
A = [1, 6, 6**2, 6**3, 6**4, 6**5, 6**6, 9, 9**2, 9**3, 9**4, 9**5]
dp = [1000000] * 300000
dp[0] = 0

for i in range(N):
    for a in A:
        d = dp[i] + 1
        dp[i + a] = min(dp[i + a], d)

print(dp[N])