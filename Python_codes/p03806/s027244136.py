dp_n = 410
n, ma, mb = map(int, input().split())
dp = [[float('inf')]*dp_n for _ in range(dp_n)]
dp[0][0] = 0
for i in range(n):
    a, b, c = map(int, input().split())
    for j in reversed(range(dp_n)):
        for i in reversed(range(dp_n)):
            if dp[i][j] != float('inf'):
                try:
                    dp[i+a][j+b] = min(dp[i+a][j+b],dp[i][j]+c)
                except:
                    pass
res = float('inf')
for j in range(1,dp_n):
    for i in range(1,dp_n):
        if i*mb == j*ma:
            res = min(res,dp[i][j])
print(res if res != float('inf') else -1)