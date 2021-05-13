n = int(input())
P = list(map(float, input().split()))

#dp[i][j] i枚投げた時にj枚表の確率
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1.0

for i in range(n):
  for j in range(i + 1):
    dp[i+1][j+1] += dp[i][j] * P[i]
    dp[i+1][j] += dp[i][j] * (1 - P[i])
    
ans = sum([dp[n][j] for j in range(n + 1) if j * 2 > n])
      
print(ans)
