#!/usr/bin python3
# -*- coding: utf-8 -*-

mod = 10**9+7
n = int(input())
seen = {}
# dp[i]: 左からi番目まで見た際の場合の数

dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    ci = input()
    j = seen.get(ci, 0)
    if j == 0:          #新しい色の追加
        dp[i]+=dp[i-1]
    elif j == i-1:      #直前と同じ
        dp[i]+=dp[i-1]
    else:
        dp[i]+=dp[i-1]  #新しい色の左以前を変える
        dp[i]+=dp[j]    #新しい色の左側を変える
        dp[i]%=mod
    seen[ci] = i
#    print(i,ci,dp,seen)
print(dp[n])