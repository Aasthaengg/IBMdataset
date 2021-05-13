# -*- coding: utf-8 -*-
#D - Number of Amidakuji
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
H,W,K = map(int,readline().split())
facts = [1,1,2,3,5,8,13,21,34]
# a = [0]
# b = [1]
# for i in range(W):
#     a.append(b[i])
#     b.append(a[i]+b[i])

dp = [0] * W
dp[0] = 1
for _ in range(H):
    ndp = [0]*W
    for w in range(W):
        ndp[w] += dp[w] * facts[w] * facts[W-w-1]
        if w > 0:
            ndp[w] += dp[w-1] * facts[w-1] * facts[W-w-1] 
        if w < W-1:
            ndp[w] += dp[w+1] * facts[w] * facts[W-w-2]
        ndp[w] %= MOD
    dp = ndp
    
print(dp[K-1])