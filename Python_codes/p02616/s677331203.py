import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
minus=[]
plus=[]
cnt=Counter(a)
zerocnt=cnt[0]
minuscnt=0
pluscnt=0
for i in range(n):
    if a[i]<0:
        minuscnt+=1
        minus.append(a[i])
    elif a[i]>0:
        pluscnt+=1
        plus.append(a[i])


if n==k:
    ans=1
    for i in range(n):
        ans*=a[i]
        ans%=mod
    print(ans%mod)
    quit()

if minuscnt==n:
    ans=1
    if k%2==0:
        for i in range(k):
            ans*=a[i]
            ans%=mod
        print(ans)
    else:
        for i in range(k):
            ans*=a[-1-i]
            ans%=mod
        print(ans)
    quit()

if minuscnt%2==1:
    minuscnt-=1

# print(minus)
plus.reverse()
# plus.append(0)
# plus.append(0)
# print(plus)

ans=1
nokori=k
m,p=0,0
# minuscnt=max(minuscnt,1)

while nokori:
    # print(pluscnt,p,m,nokori)
    if m==minuscnt:
        if p!=pluscnt:
            ans*=plus[p]
            p+=1
            nokori-=1
        else:
            ans=0
            nokori=0
    elif p==pluscnt:
        if nokori==1:
            ans=0
            nokori-=1
        else:
            ans*=minus[m]*minus[m+1]
            m+=2
            nokori-=2
    elif p+1==pluscnt:
        if nokori%2==0:
            ans*=minus[m]*minus[m+1]
            m+=2
            nokori-=2
            # if nokori==1:
        else:
            ans*=plus[p]
            p+=1
            nokori-=1
            # elif plus[p]>minus[m]*minus[m+1]:
            #     ans*=plus[p]
            #     p+=1
            #     nokori-=1
            # else:
            #     ans*=minus[m]*minus[m+1]
            #     m+=2
            #     nokori-=2
    elif nokori==1:
        ans*=plus[p]
        nokori-=1
    elif plus[p]*plus[p+1]>minus[m]*minus[m+1]:
        # if nokori%2==0:
        #     ans*=plus[p]*plus[p+1]
        #     p+=2
        #     nokori-=2
        # else:
        ans*=plus[p]
        p+=1
        nokori-=1
    else:
        ans*=minus[m]*minus[m+1]
        m+=2
        nokori-=2
    ans%=mod
print(ans%mod)
