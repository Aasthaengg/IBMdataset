import sys
from collections import deque
import time
import bisect
def input():
    return sys.stdin.readline()[:-1]
mod=1000000007
h,w,k=map(int,input().split())
n=2**(w-1)
if w==1:
    print(1)
    exit()

dp=[[0]*w for i in range(h+1)]
dp[0][0]=1

# print(tyuo)
# print(haji)
for l in range(h):
    for i in range(1<<w-1):
        a = str(bin(i))[2:].zfill(w-1)
        if a.count('11') >= 1:
            continue
        for j in range(w):
            if j==0:
                if i & (1<<w-2):
                    dp[l+1][j+1]+=dp[l][j]
                else:
                    dp[l+1][j]+=dp[l][j]
            elif j==w-1:
                if i & 1:
                    dp[l+1][j-1]+=dp[l][j]
                else:
                    dp[l+1][j]+=dp[l][j]
            else:
                if i & (1<<j-1):
                    dp[l+1][j-1]+=dp[l][j]
                elif i & (1<<j):
                    dp[l+1][j+1]+=dp[l][j]
                else:
                    dp[l+1][j]+=dp[l][j]
            # print(i,dp[l+1])
# print(dp)
print(dp[h][k-1]%mod)