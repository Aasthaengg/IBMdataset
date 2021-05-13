import bisect, copy, heapq, math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))

kakutei=[-1]*n
kakutei[0]=t[0]
kakutei[-1]=a[-1]
for i in range(n-1):
    if t[i]<t[i+1]:
        kakutei[i+1]=t[i+1]
    if a[-2-i]>a[-1-i]:
        kakutei[-2-i]=a[-2-i]
# print(kakutei)
ans=1
if n==1 and t[0]!=a[0]:
    ans=0
for i in range(n):
    if kakutei[i]>min(t[i],a[i]):
        ans=0

for i in range(n):
    if kakutei[i]==-1:
        ans*=min(t[i],a[i])
    ans%=mod

print(ans)