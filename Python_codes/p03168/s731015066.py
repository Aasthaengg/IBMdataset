n = int(input())
a = list(map(float, input().split()))
ans = 0
if n == 1:
    ans = a[0]
else:
    dp = [[0]*(n//2+1) for _ in range(n)]
    dp[0][0] = a[0]
    dp[0][1] = 1-a[0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0]*a[i]
        for j in range(1, n//2+1):
            dp[i][j] = dp[i-1][j]*a[i] + dp[i-1][j-1]*(1-a[i])
    ans = sum(dp[-1])
print(ans)