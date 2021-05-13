from collections import deque
from bisect import bisect_left
S = input()
# dp[i][j]はうしろからi桁を13で割った余りがjであるものの個数
dp = [[0] * 13 for _ in range(len(S) + 1)]
dp[0][0] = 1
mul = 1
mod = 10**9 + 7

for i in range(len(S)):
  x = S[-(i+1)]
  if x == '?':
    for k in range(10):
      for j in range(13):
        dp[i+1][(mul*k+j)%13] += dp[i][j]
        dp[i+1][(mul*k+j)%13] %= mod
  else:
    k = int(x)
    for j in range(13):
      dp[i+1][(mul*k+j)%13] += dp[i][j]
      dp[i+1][(mul*k+j)%13] %= mod
  mul = mul*10 % 13  
print(dp[len(S)][5])