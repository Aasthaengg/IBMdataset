import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
v = []
t = []

for _ in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    v.append(a)
    ti = 0
    
    for i in range(b):
        ti += 1<<(c[i]-1)
    
    t.append(ti)

dp = [10**18]*(1<<N)
dp[0] = 0

for S in range(1<<N):
    for i in range(M):
        dp[S|t[i]] = min(dp[S|t[i]], dp[S]+v[i])

if dp[-1]==10**18:
    print(-1)
else:
    print(dp[-1])