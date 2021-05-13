n, m = map(int, input().split())
l = list(map(int, input().split()))
dp = [10**5] * (n+1)
dp[0] = 0
for i in range(len(l)):
    m = l[i]
    for j in range(m,n+1):
        dp[j] = min(dp[j-m]+1, dp[j])
print(dp[n])
