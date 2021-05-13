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

n=int(input())
a=list(map(int,input().split()))
cnt1=0
now=0
for i in range(n):
    now+=a[i]
    if i%2==0:
        if now<=0:
            cnt1+=1-now
            now=1
    else:
        if now>=0:
            cnt1+=now+1
            now=-1
cnt2=0
now=0
for i in range(n):
    now+=a[i]
    if i%2==1:
        if now<=0:
            cnt2+=1-now
            now=1
    else:
        if now>=0:
            cnt2+=now+1
            now=-1

print(min(cnt1,cnt2))