n = int(input())

dp = [10**6 for _ in range(10**6)]
dp[0] = 0

for i in range(n):
    j6 = 1
    while j6 <= n:
        dp[i+j6] = min(dp[i+j6],dp[i]+1)
        j6 *= 6
    j9 = 1
    while j9 <= n:
        dp[i+j9] = min(dp[i+j9],dp[i]+1)
        j9 *= 9
print(dp[n])