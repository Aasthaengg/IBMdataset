# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

R, C, K = map(int, readline().split())
data = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    r,c,k = map(int,readline().split())
    data[r][c] = k
    
dp = [0]*(C+1)

for i in range(1,R+1):
    di = data[i]
    ndp = [0]*(C+1)
    kdp = [0]*4
    for j in range(1,C+1):
        kdp[0] = max(kdp[0],dp[j])
        for k in range(2,-1,-1):
            kdp[k+1] = max(kdp[k+1],kdp[k]+di[j])
        ndp[j] = max(kdp)
    dp = ndp
print(dp[C])