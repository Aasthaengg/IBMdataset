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
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
b=list(map(int,input().split()))

anslst=[]
while b:
    for i in range(len(b))[::-1]:
        if b[i]==i+1:
            anslst.append(b[i])
            b.pop(i)
            break
    else:
        print(-1)
        quit()
# print(anslst)
for i in range(n):
    print(anslst[-1-i])