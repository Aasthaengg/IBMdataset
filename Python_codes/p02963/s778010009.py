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

s=int(input())
# x=(10**9-s%(10**9))%(10**9)
# y=(s+x)//(10**9)
y=math.ceil(s/(10**9))
x=(10**9)*y-s
print(0, 0, 10**9,1,x,y)
# print(10**9,1)
# print(10**9-s%(10**9),s//(10**9))