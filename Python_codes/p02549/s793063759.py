#!/usr/bin/env python

n, k = map(int, input().split())
L = [0 for _ in range(k)]
R = [0 for _ in range(k)]
for i in range(k):
    L[i], R[i] = map(int, input().split())
mod = 998244353

dp = [0 for _ in range(n+1)]
dp[1] = 1 
cumsum = [0 for _ in range(n+1)]
cumsum[1] = 1 

# O(NK)
for i in range(2, n+1):
    for j in range(k):
        li = i-R[j]
        ri = i-L[j]
        if ri<0: continue
        li = max(li, 1)
        dp[i] += (cumsum[ri]-cumsum[li-1])%mod
    cumsum[i] = cumsum[i-1]+dp[i]

print(dp[n]%mod)
