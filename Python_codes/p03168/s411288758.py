import math

n = int(input())
lst = list(map(float, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)] #行は表の枚数、列は試行回数
dp[0][0] = 1
for i in range(0, n):
    for j in range(0, n):
        dp[i+1][j+1] += dp[i][j] * lst[i] #表のとき
        dp[i+1][j] += dp[i][j] * (1 - lst[i]) #裏のとき
        
hlf = math.ceil(n/2)
ansl = dp[n][hlf:n+1]
ans = sum(ansl)
print(ans)