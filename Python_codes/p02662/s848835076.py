##WA 和がSになる組み合わせを列挙しようとしたけど無理だった。
ma = lambda :map(int,input().split())
ni = lambda:int(input())
import collections
import math
import itertools
gcd = math.gcd
mod = 998244353
n,s = ma()
A = list(ma())
dp = [[0]*(s+1) for i in range(n+1)]#dp[i][j]はi番目までの要素を用いてjになるような場合の数
dp[0][0] = 1
for i in range(n):
    a = A[i]
    for j in range(s+1):
        dp[i+1][j] =(dp[i][j]*2)%mod
        if a<=j:
            dp[i+1][j] = (dp[i][j-a] +dp[i+1][j]) %mod

print(dp[n][s])
#print(dp)
