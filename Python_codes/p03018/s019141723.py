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

s=input()
n=len(s)
lst=[0]*n
for i in range(n):
    lst[i]=s[i]


ans=0
cnt=0
i=0
while i<n-2:
    if lst[i]=="A":
        cnt+=1
    else:
        cnt=0
    if lst[i]=="A" and lst[i+1]=="B" and lst[i+2]=="C":
        ans+=cnt
        cnt-=1
        lst[i+2]="A"
        i+=1
    # print(lst)
    # print(i,ans,cnt)
    i+=1
print(ans)
# print(lst)