import sys
import math
import bisect
def input():
    return sys.stdin.readline()[:-1]
n,t=map(int,input().split())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))

dp = [[0 for i in range(t)]for i in range(n+1)]
ab = sorted(ab,key=lambda x:x[0])
ans = ab[0][1]
for i in range(1,n):
    for j in range(t):
        if j-ab[i-1][0]>=0:
            dp[i][j] += max(dp[i-1][j-ab[i-1][0]] + ab[i-1][1],dp[i-1][j])
        else:
            dp[i][j] += dp[i-1][j]

    ans = max(ans,dp[i][-1]+ab[i][1])

print(ans)
