import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
a=list(map(int,input().split()))

tmp=[0,abs(a[0])]
for i in range(n):
    if tmp[1]<abs(a[i]):
        tmp[0]=i
        tmp[1]=abs(a[i])
# print(tmp)

lst=[]

for i in range(n):
    a[i]+=a[tmp[0]]
    lst.append([tmp[0]+1,i+1])

# print(a[tmp[0]])
if a[tmp[0]]<0:
    for i in range(n-1):
        a[-2-i]+=a[-1-i]
        lst.append([n-i,n-i-1])
else:
    for i in range(n-1):
        a[i+1]+=a[i]
        lst.append([1+i,2+i])
# print(a)
# print(lst)
print(len(lst))
for i in lst:
    print(*i)