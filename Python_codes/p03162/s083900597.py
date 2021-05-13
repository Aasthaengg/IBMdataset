n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp=[[0,0,0] for n in range(n + 1)]
# dp = [[0] * 3] * (n + 1)

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i +1][k] = max(dp[i + 1][k], dp[i][j] + a[i][k])
                
res = 0
for j in range(3):
    res = max(res, dp[n][j])
print(res)