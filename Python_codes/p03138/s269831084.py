# -*- coding: utf-8 -*-
#D - XXOR
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K = map(int, readline().split())
A = list(map(int,readline().split()))

dp = [[0]*2 for i in range(41)]

for i in range(1,41):
    cnt = 0
    for j in range(N):
        cnt += 1 if (A[j] >> (40-i)) & 1 else 0
    if dp[i-1][1] == 1:
        dp[i][1] = 1
    if cnt >= N-cnt:
        #i行目は0にする
        dp[i][0] = dp[i-1][0] + 2**(40-i) * cnt
        if (K >> (40-i)) & 1 == 1:
            dp[i][1] = 1
    else:
        #i行目は1にしたい
        if dp[i][1] == 1:
            #1にする
            dp[i][0] = dp[i-1][0] + 2**(40-i)*(N-cnt)
        else:
            if (K >> (40-i))&1 == 1:
                #1にする
                dp[i][0] = dp[i-1][0] + 2**(40-i)*(N-cnt)
            else:
                #1にできないので0にする
                dp[i][0] = dp[i-1][0] + 2**(40-i)*cnt
print(dp[-1][0])