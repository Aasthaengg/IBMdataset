import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

n=int(input())
a=list(map(int,input().split()))
a.sort()

lst=[]

flag=0
for i in range(n-1):
    if a[i+1]>0:
        flag=i+1
        break
if flag==0:
    flag=n-1
tmp=a[0]
for i in range(flag,n-1):
    lst.append([tmp,a[i]])
    tmp-=a[i]
a[0]=tmp
tmp=a[-1]
for i in range(flag):
    lst.append([tmp,a[i]])
    tmp-=a[i]

print(tmp)
for i in range(n-1):
    print(*lst[i])
    
# print(lst)