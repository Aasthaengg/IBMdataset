#ABC130-E Common Subsequence
"""
問題：
整数列のリストが与えられる
空であるものも含めて、sとtの部分列として等しいものの個数を求めよ
解法：
LCSのmaxではなくsumのバージョンでかつ、
数え上げなので重複をなくさなければならない。
具体的には、
dp[i][j]:sをi文字目迄見た時のtをj文字目迄見た時に、
dp0:横方向(j方向)を優先して遷移した後に、縦方向(i方向)への遷移を行った時の合計
dp1:縦方向、横方向への遷移を行った時の合計
として、dp1[-1][-1]が答え。

"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m = map(int,readline().split())
s = list(map(int,readline().split())) + [-1]
t = list(map(int,readline().split())) + [-2]
mod = 10**9+7

#dp table
dp0 = [[0]*(m+2) for _ in range(n+2)]
dp1 = [[0]*(m+2) for _ in range(n+2)]
dp0[0][0] = 1
#process1
for i in range(n+1):
    for j in range(m+1):
        dp0[i+1][j] += dp0[i][j]%mod
        dp1[i][j] += dp0[i][j]%mod
        dp1[i][j+1] += dp1[i][j]%mod
        if s[i] == t[j]:
            dp0[i+1][j+1] += dp1[i][j]%mod


print(dp1[n][m]%mod)
