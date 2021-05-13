inf = float('inf')

n,m = map(int,input().split())
c = list(map(int,input().split()))

dp = [inf]*(n+1)
dp[0] = 0
for i in range(1,n+1):
    for ci in c:
        if i - ci >= 0:
            dp[i] = min(dp[i], dp[i-ci] + 1)

ans = dp[n]
print(ans)
