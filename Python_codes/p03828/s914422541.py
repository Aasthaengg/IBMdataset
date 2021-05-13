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

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

n=int(input())
if n==1:
    print(1)
    exit()
d=defaultdict(int)
for i in range(2,n+1):
    tmp=factorization(i)
    for j in tmp:
        yaku,ko=j
        d[yaku]+=ko
# print(d)
ans=1
for i in d.values():
    ans*=i+1
    ans%=mod
print(ans)