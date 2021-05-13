import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]


s=input()
ans=0
cnt=0
for i in range(len(s)):
    if s[i]=="B":
        cnt+=1
    else:
        ans+=cnt
print(ans)