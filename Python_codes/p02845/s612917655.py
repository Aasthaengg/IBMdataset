n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7
dp = [[0]*3 for _ in range(n+1)]
ans = 1
for i in range(n):
    ans *= dp[i].count(a[i])
    ans %= mod
    for j in range(3):
        dp[i+1][j] = dp[i][j]
        if dp[i][j] == a[i]:
            dp[i+1][j] += 1
            a[i] = -1
print(ans)