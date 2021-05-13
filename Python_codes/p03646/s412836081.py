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

k=int(input())
if k==0:
    print(2)
    print("1 1")
elif k==1:
    print(2)
    print("2 0")
elif k>=50:
    syou=k//50
    amari=k%50
    print(50)
    lst=[49+syou-1]*50
    lst[0]+=1
    for i in range(50):
        if i<amari:
            lst[i]+=50-amari+1
        else:
            lst[i]-=amari
    print(" ".join(map(str,lst)))
else:
    print(k)
    lst=[[] for i in range(k)]
    lst[0]=k
    for i in range(k-1):
        lst[i+1]=k-1
    print(" ".join(map(str,lst)))