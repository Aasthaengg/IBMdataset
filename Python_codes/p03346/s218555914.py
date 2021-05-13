import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

n=int(input())
p=[int(input()) for i in range(n)]
lst=[0]*(n+2)
for i in range(n):
    lst[p[-1-i]]=lst[p[-1-i]+1]+1
# print(lst)
print(n-max(lst))