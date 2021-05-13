# -*- coding: utf-8 -*-
N,W = list(map(int,input().split()))
vw = [list(map(int,input().split())) for i in range(N)]
vw.sort(key = lambda x:x[0])
value = [i[1] for i in vw]
weight = [i[0] for i in vw]
#valueが最大の要素を事前に抽出


inf=float("inf")
dp = [[-inf for _ in range(W+1)] for _ in range(N+1)]

dp[0] = [0]*(W+1)
def nap():
    for i in range(N):
        w = 0
        while w <= W:
            if weight[i] <= w:
                dp[i+1][w]=max(dp[i][w-weight[i]]+value[i],dp[i][w])
            else:
                dp[i+1][w]=dp[i][w]
            w+=1
nap()

ret = 0
for i in range(N):
    ret = max(ret,dp[i][W-1]+value[i])
print(ret)