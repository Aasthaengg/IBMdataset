import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

s=input()
ab=[0,0]
ans=0
cnt=0
for i in range(len(s)):
    if s[i]=="A":
        ab[0]+=pow(3,cnt,mod)
    elif s[i]=="B":
        ab[1]+=ab[0]
    elif s[i]=="C":
        ans+=ab[1]
    else:
        ans=ab[1]+3*ans
        ab[1]=ab[0]+3*ab[1]
        ab[0]=pow(3,cnt,mod)+3*ab[0]
        cnt+=1
    ab[0]%=mod
    ab[1]%=mod
    ans%=mod
print(ans%mod)
