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

n=int(input())
a=list(map(int,input().split()))
lst=[0]*n
for i in range(n):
    lst[a[i]]+=1

for i in range(n):
    if n%2==0:
        if i%2==0 and lst[i]!=0:
            break
        elif i%2==1 and lst[i]!=2:
            break
    else:
        if i%2==1 and lst[i]!=0:
            break
        elif i%2==0:
            if i==0:
                if lst[i]!=1:
                    break
            elif lst[i]!=2:
                break
else:
    print(pow(2,n//2,mod))
    exit()
print(0)