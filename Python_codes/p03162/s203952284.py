n = int(input())
dp = []
for _ in range(n):
  dp.append(list(map(int,input().split())))

for j in range(1,n):
    dp[j][0] += max(dp[j-1][1],dp[j-1][2])
    dp[j][1] += max(dp[j-1][0],dp[j-1][2])
    dp[j][2] += max(dp[j-1][0],dp[j-1][1])

print(max(dp[-1]))