import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n,k=map(int,input().split())
dp=[0]*n
sdp=[0]*(n+1)
sdp[1]=1
dp[0]=1
mod=998244353
lr=[list(map(int,input().split())) for _ in range(k)]
for i in range(1,n):
    for j in range(k):
        l,r=lr[j]
        left=max(0,i-r)
        right=max(0,i-l+1)
        dp[i]+=(sdp[right]-sdp[left])
        dp[i]%=mod
    sdp[i+1]=(sdp[i]+dp[i])%mod
print(dp[-1])
        
