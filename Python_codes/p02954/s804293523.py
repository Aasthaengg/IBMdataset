import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

s=input()
n=len(s)
anslst=[0]*n

cnt=0
for i in range(n):
    if s[i]=="R":
        cnt+=1
    else:
        anslst[i]+=cnt//2
        anslst[i-1]+=(cnt+1)//2
        cnt=0

for i in range(n):
    if s[-i-1]=="L":
        cnt+=1
    else:
        anslst[-i-1]+=cnt//2
        anslst[-i]+=(cnt+1)//2
        cnt=0

print(*anslst)