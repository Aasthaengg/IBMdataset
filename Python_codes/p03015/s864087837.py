# -*- coding: utf-8 -*-
#E - Sum Equals Xor
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
L = readline().decode().rstrip()
S = len(L)

# dp[i][j] : 上からi桁目の数まで見たとき,L以下であることがj(0:未確定/1:確定)
#            であるような条件を満たす組の総数
# S[i] == 0のとき
#   未確定 dp[i-1][0] → (0,0)の1通り  
#   確定 dp[i-1][1] → (0,0)(0,1)(1,0)の3通り
# S[i] == 1のとき
#   未確定 dp[i-1][0] → (0,1)(1,0)の2通り  
#   確定 dp[i-1][1] → (0,0)(0,1)(1,0)の3通り
#       dp[i-1][0] → (0,0)の1通り

dp = [[0]*2 for _ in range(S+1)]
dp[0][0] = 1

for i,l in enumerate(L,1):
    if l == '0':
        dp[i][0] = dp[i-1][0] % MOD
        dp[i][1] = 3*dp[i-1][1] % MOD
    else:
        dp[i][0] = 2*dp[i-1][0] % MOD
        dp[i][1] = (3*dp[i-1][1]+dp[i-1][0]) % MOD

print(sum(dp[-1])%MOD)