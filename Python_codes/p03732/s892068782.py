ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys
n,W = ma()
wm=3*(n-1)
dp=[[[0]*(wm+1) for j in range(n+1)] for j in range(n+1) ] #dp[i][j][w] iまで見てj個使った時に重さwとなる場合のmaxのv
wv=[]
for i in range(n):
    w,v=ma()
    if i==0:
        wv.append((0,v))
        w0=w
    else:
        wv.append((w-w0,v))

for i in range(n):
    w,v = wv[i]
    for j in range(1,i+2):
        #print(i,j)
        for ww in range(wm+1):
            dp[i][j][ww]=dp[i-1][j][ww]
            if ww-w>=0:
                dp[i][j][ww]=max(dp[i-1][j-1][ww-w]+v,dp[i][j][ww])
ans=0
for j in range(n+1):
    for w in range(wm+1):
        if j*w0 + w<=W:
            ans=max(ans,dp[n-1][j][w])
print(ans)
# print(wv)
# for i in range(n):
#     print(dp[i])
#     print()
