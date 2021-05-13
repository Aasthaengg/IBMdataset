import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations
from itertools import accumulate
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

n=int(input())
c=[int(input()) for i in range(n)]
dp=[0]*n
dic={}
dp[0]=1
dic[c[0]]=1
for i in range(1,n):
    if c[i]==c[i-1]:
        dp[i]=dp[i-1]
        continue
    if c[i] in dic:
        dp[i]=(dp[i-1]+dic[c[i]])%mod
        dic[c[i]]=dp[i]
    else:
        dp[i]=dp[i-1]%mod
        dic[c[i]]=dp[i]
print(dp[-1]%mod)
# print(dic)