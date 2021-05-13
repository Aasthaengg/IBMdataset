import sys
input = sys.stdin.readline
from collections import *

N, K = map(int, input().split())
ans = 0
cnt = [0]*(K+1)
MOD = 10**9+7

for i in range(K, 0, -1):
    cnt[i] = pow(K//i, N, MOD)
    
    for j in range(2*i, K+1, i):
        cnt[i] -= cnt[j]
        cnt[i] %= MOD
    
    ans += i*cnt[i]
    ans %= MOD

print(ans)