n = int(input())

dp = [False]*110
dp[4] = dp[7] = True

for i in range(101):
  if dp[i]:
    dp[i+4] = True
    dp[i+7] = True
  
if dp[n]:
  print("Yes")
else:
  print("No")