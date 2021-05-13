#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

number = [0,2,5,5,4,5,6,3,7,6]

N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

dp = [-1]*(N+1)
dp[0] = 0
for i in range(N+1):
    for a in A:
        if i-number[a] >= 0:
            if dp[i-number[a]] >= 0:
                dp[i] = max(dp[i], dp[i-number[a]]*10+a)

print(dp[N])