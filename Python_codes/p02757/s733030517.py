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

n,p=map(int,input().split())
s=input()

ans=0

if p==2 or p==5:
    for i in range(n):
        if int(s[i])%p==0:
            ans+=i+1
else:
    lst=[0]*(n+1)
    for i in range(n):
        lst[-2-i]=(lst[-1-i]+int(s[-1-i])*pow(10,i,p))%p
    # print(lst)
    cnt=Counter(lst)
    for i in range(n):
        cnt[lst[i]]-=1
        ans+=cnt[(lst[i]-p)%p]
        # cnt[lst[i]]-=1
    #     print(ans)
    # print(cnt)
print(ans)