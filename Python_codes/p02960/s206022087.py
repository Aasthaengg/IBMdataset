import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())[::-1]
leng = len(S)
mod = 10**9+7

old_dp = [0]*13
old_dp[0] = 1

for i in range(leng):
    dp = [0]*13
    if S[i]!='?':
        d = int(S[i])
        d = d*pow(10, i, 13)
        for j in range(13):
            dp[j] += old_dp[(j-d)%13]
            dp[j] %= mod
    else:
        for d in range(10):
            d = d*pow(10, i, 13)
            for j in range(13):
                dp[j] += old_dp[(j-d)%13]
                dp[j] %= mod
    old_dp = dp

print(dp[5])