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

n,m=map(int,input().split())
a=list(map(int,input().split()))
lst=[0]+list(accumulate(a))
# print(lst)
dic=defaultdict(int)
for i in range(n+1):
    dic[lst[i]%m]+=1
# print(dic)
lis2=list(dic.items())
# print(lis2)
ans=0
for i in lis2:
    ans+=i[1]*(i[1]-1)//2
print(ans)