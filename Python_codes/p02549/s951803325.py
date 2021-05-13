#
import sys
import math
import itertools

# 整数をいくつか入力
n,k = (int(i) for i in input().split())


lr = [[int(i) for i in input().split()] for i in range(k)] 

dp  = [0] * (n+1)
ans = [0] * (n+1)
dp[1]=1
ans[1]=1

for i in range(2,n+1):
    for a in lr:
        if a[0] < i:
            dp[i] += ans[i-a[0]]
            if a[1] < i-1:
                dp[i] -= ans[i-a[1]-1]
    dp[i] = dp[i] % 998244353
    ans[i]=ans[i-1]+dp[i]

print(dp[n]%998244353)

