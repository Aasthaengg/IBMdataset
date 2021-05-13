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

h,w,k=map(int,input().split())
s=[input() for i in range(h)]
# print(s)
ans=float('inf')
for i in range(2**(h-1)):
    tmp=1
    for j in range(h-1):
        if 1 & (i>>j):
            tmp+=1
    lst=[[0]*tmp for j in range(w)]

    for j in range(w):
        now=0
        for l in range(h):
            if s[l][j]=="1":
                lst[j][now]+=1
            if 1 & (i>>l):
                now+=1

    cnt=[0]*tmp
    cutcnt=0
    for j in range(w):
        flag=0
        for l in range(tmp):
            if cnt[l]+lst[j][l]>k:
                flag=1
    
        if flag==0:
            for l in range(tmp):
                cnt[l]+=lst[j][l]
        else:
            cutcnt+=1
            for l in range(tmp):
                cnt[l]=lst[j][l]
                if cnt[l]>k:
                    cutcnt=float('inf')
        # print(cnt)
    ans=min(cutcnt+tmp-1,ans)
    # print(lst)
    # print(cutcnt,tmp-1)
print(ans)