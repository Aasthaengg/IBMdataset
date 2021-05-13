n,t = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key = lambda x: x[0])

dp = [[0]*(t+3001) for _ in range(n+1)]

for i in range(n):
    a,b = ab[i]
    for j in range(t):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    for j in range(t+ab[i][0]):
        if j + a <= t+3000:
            dp[i+1][j+a] = max(dp[i+1][j+a], dp[i][j] + b)

ans = 0

for i in range(n):
    ans = max(ans, max(dp[i+1][:t+ab[i][0]]))

print(ans)
