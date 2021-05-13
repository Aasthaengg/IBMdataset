n = int(input())
p = list(map(float,input().split()))

dp = [[0]*3100 for _ in range(3100)]

dp[0][0] = 1

# dp[i][j] := 最初の i 枚のコインを投げたときに、表が j 枚となる確率

for i in range(n):
    for j in range(i+1):
        dp[i+1][j+1] += dp[i][j] * p[i]
        dp[i+1][j] += dp[i][j] * (1-p[i])

res = 0
for j in range(n//2+1,n+1):
    res += dp[n][j]
print(res)