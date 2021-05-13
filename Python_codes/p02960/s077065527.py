import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

S = readline().rstrip()
S = S[::-1]
dp = [0]*13
dp[0] = 1
pow10 = 4
for i,s in enumerate(S):
    dpnew = [0]*13
    pow10 = (pow10*10)%13
    if s != '?':
        k = int(s)
        for j in range(13):
            dpnew[(k*pow10+j)%13] = (dpnew[(k*pow10+j)%13]+dp[j])%mod
    else:
        for k in range(10):
            for j in range(13):
                dpnew[(k*pow10+j)%13] = (dpnew[(k*pow10+j)%13]+dp[j])%mod
    dp = dpnew

print(dp[5])

