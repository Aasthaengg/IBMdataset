S = int(input())
  
#初期化
dp = [0]*S
if S > 2:
  dp[2] = 1
  dp_S = 0

#dp
  for i in range(3,S):
    dp_S += dp[i-3] 
    dp[i] = 1+dp_S

print(dp[S-1]%1000000007)