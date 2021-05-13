n = int(input())
al = list(map(int, input().split()))
l = 0
r = n-1

data = [[i, a] for i, a in enumerate(al)]
data.sort(key=lambda x: x[1], reverse=True)
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(0, i+1):
        p, a = data[i]
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + abs(n-1-j-p)*a)
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + abs(i-j-p)*a)
print(max(dp[-1]))
