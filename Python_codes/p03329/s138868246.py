coin = [1,
6,6**2,6**3,6**4,6**5,6**6,
9,9**2,9**3,9**4,9**5]
n = int(input())
inf = 10**9
dp = [inf]*(n+1)
dp[0] = 0
for c in coin:
    for yen in range(c, n+1):
        dp[yen] = min(dp[yen], dp[yen-c] + 1)
print(dp[n])
