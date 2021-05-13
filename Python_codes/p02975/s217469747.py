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

n=int(input())
a=list(map(int,input().split()))

cnt=Counter(a)
if cnt[0]==n:
    print("Yes")
    quit()
if n%3!=0:
    print("No")
    quit()
a.sort()
if cnt[0]==n//3 and cnt[a[-1]]==2*n//3:
    print("Yes")
    quit()

# print(1)
lst=[]
for i in range(n):
    if cnt[a[i]]==n//3:
        if a[i] in lst:
            continue
        else:
            lst.append(a[i])
    else:
        print("No")
        quit()
if lst[0]^lst[1]^lst[2]==0:
    print("Yes")
    quit()
else:
    print("No")