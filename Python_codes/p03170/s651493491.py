n,k = map(int,input().split())
a = [int(i) for i in input().split()]

dp = [0]*(k+1)
dp[0] = 0

for i in range(1,k+1):
  for j in range(n):
    if i-a[j] >= 0 and dp[i-a[j]] == 0:
      dp[i] = 1
      break
    #dp[i] = 0

if dp[k] == 1:
  print("First")
else:
  print("Second")
