# numpyでかいてもTLEした。
# pypyでlistでかくととおる？

#import numpy as np
N,M = list(map(int, input().split()))
S = list(map(int, input().split()))
T = list(map(int, input().split()))
mod = int(1e9+7)
"""
dp[i][j] : S の i 文字目までと T の j 文字目までを考慮し、
この 2 文字 (S[i] と T[j]）をペアにするときの場合の数とすると、

dp[i][j] = (sum(dp[1:i-1][1:j-1]) + 1 if S[i] == T[j] else 0)
このsumの部分をどうもとめるか。

最終的な答えはsum(dp[:][:])。

2-D cumsumをつかう
i,j = 0のときにきをつけて
DS[i][j] = DS[i-1][j] + DS[i][j-1] - DS[i-1][j-1] + dp[i][j]
"""

dp = [[ 0 for _ in range(M)] for _ in range(N)]
DS = [[ 0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
  for j in range(M):
    if S[i] != T[j]:
      dp[i][j] = 0
    else:
      dp[i][j] += 1
      dp[i][j] += DS[i-1][j-1]
      dp[i][j] %= mod
    DS[i][j] = DS[i-1][j] + DS[i][j-1] - DS[i-1][j-1] + dp[i][j]
    DS[i][j] %= mod
print(DS[-2][-2]+1)
#print(dp)
#print(DS)
