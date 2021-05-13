import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7

l=input()
# print(l)
dp1=[0]*(len(l)+1)
dp2=[0]*(len(l)+1)
dp1[0]=1
for i in range(len(l)):
    if l[i]=="1":
        dp1[i+1]+=dp1[i]*2
        dp2[i+1]+=dp1[i]
        dp2[i+1]+=dp2[i]*3
    else:
        dp1[i+1]+=dp1[i]
        dp2[i+1]+=dp2[i]*3
    dp1[i+1]%=mod
    dp2[i+1]%=mod
# print(dp1)
# print(dp2)
print((dp1[-1]+dp2[-1])%mod)