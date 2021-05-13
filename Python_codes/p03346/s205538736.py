import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
P = [int(input()) for _ in range(N)]
idx = defaultdict(int)

for i in range(N):
    idx[P[i]] = i
    
dp = [0]*N

for i in range(N):
    if P[i]==1:
        dp[i] = 1
    else:
        dp[i] = dp[idx[P[i]-1]]+1
    
print(N-max(dp))