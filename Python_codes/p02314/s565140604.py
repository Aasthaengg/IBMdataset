n,m = map(int, input().split())
cs = list(map(int, input().split()))
dp = [float("inf")]*(n+1)
dp[0] = 0
for i in range(n+1):
    for c in cs:
        if i+c < n+1:
            dp[i+c] = min(dp[i+c], dp[i]+1)
print(dp[n])
