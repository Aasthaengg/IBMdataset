# -*- coding: utf-8 -*-
"""
Created on Sat May 26 12:16:54 2018
DPL-1A Rec Call Revised
@author: maezawa
"""

n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
c.sort()
dp = [float('inf') for _ in range(n+1)]
dp[0] = 0
#print(n,m)
#print(c)
#print(*dp, sep='\n')

for j in range(1,n+1):
    temp = []
    for i in range(m):
        if j < c[i]:
            continue
        else:
            temp.append(dp[j-c[i]]+1)
    dp[j] = min(temp)

print(dp[n])
