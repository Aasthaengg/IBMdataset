# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意MOD = 10**9+7

h,w,k = [int(i) for i in readline().split()]
MOD = 10**9+7

num =[0]*(w-1)
total = 0
for i in range(1<<(w-1)):
    for j in range(w-2):
        if ((i>>j)&1) & ((i>>(j+1))&1): break
    else:
        total += 1
        for j in range(w-1):
            if ((i>>j)&1): num[j] += 1



#dp[i][j] iまで見て位置j
dp = [[0]*(w) for i in range(h+1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        r=l=0
        if j < w-1: r = num[j]
        if j: l = num[j-1]

        if r:
            dp[i+1][j+1] += r*dp[i][j]
            dp[i+1][j+1] %= MOD
        dp[i+1][j  ] += (total-r-l)*dp[i][j]
        dp[i+1][j  ] %= MOD
        if l:
            dp[i+1][j-1] += l*dp[i][j]
            dp[i+1][j-1] %= MOD

#print(dp)
#print(total, num)
print(dp[-1][k-1])








