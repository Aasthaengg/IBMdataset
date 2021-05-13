x = int(input())
dp = [False]*101000
dp[0] = True
l = [100, 101, 102, 103, 104, 105]
for i in range(100001):
  for j in l:
    if dp[i]:
      dp[i+j] = True
if dp[x]:
  print(1)
else:
  print(0)