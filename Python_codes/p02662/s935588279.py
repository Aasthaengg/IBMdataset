N, S = map(int, input().split())
A = map(int, input().split())
 
def solve(length, target, nums):
  
  dp = [[0]*(target+1) for i in range(length+1)]
  dp[0][0] = 1
  for i, n in enumerate(nums):
    for j, comb_num in enumerate(dp[i]):
      sub = j - n
      dp[i + 1][j] += comb_num * 2
      #print(i, j, sub, dp[i])
      if sub >= 0:
        dp[i + 1][j] += dp[i][sub]
      dp[i + 1][j] %= 998244353
  #print(dp)
  print(dp[length][target])
  
solve(N, S, A)