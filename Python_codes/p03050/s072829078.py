import sys
from collections import *
import heapq
import math

import bisect
import copy
from itertools import permutations,accumulate,combinations,product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())

ans=0
# cnt=0
if n==1:
    print(0)
    quit()
for i in range(int(n**0.5)):
    x=(n-(i+1))//(i+1)
    if n//x==n%x:
        ans+=x
    # print(n//cnt,cnt)
print(ans)