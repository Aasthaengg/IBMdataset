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
al=[chr(ord('a') + i) for i in range(26)]

n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

tmp1=0
tmp2=0
for i in range(n-1):
    tmp1+=(i+1)*(n-1-i)*(x[i+1]-x[i])
    tmp1%=mod
for j in range(m-1):
    tmp2+=(j+1)*(m-1-j)*(y[j+1]-y[j])
    tmp2%=mod
# print(tmp1,tmp2)

print(tmp1*tmp2%mod)