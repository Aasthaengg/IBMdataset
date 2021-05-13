S = int(input())

if S == 1 or S ==2:
  print(0)
elif S == 3 or S == 4 or S == 5:
  print(1)
else:
  #初期化
  dp = [0]*S
  dp[2] = 1
  dp[3] = 1
  dp[4] = 1
  dp_S = 0
  #dp
  for i in range(5,S):
    dp_S += dp[i-3] 
    dp[i] = 1+dp_S

  print(dp[S-1]%1000000007)