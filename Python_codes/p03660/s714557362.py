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
ab=[list(map(int,input().split())) for i in range(n-1)]
dic=defaultdict(list)
for i in range(n-1):
    a,b=ab[i]
    dic[a].append(b)
    dic[b].append(a)
# print(dic)

lst=[0]*(n+1)
f=deque([1])
s=deque([n])
fcnt,scnt=0,0
while 1:
    flag=0
    for i in range(len(f)):
        tmp=f.popleft()
        if lst[tmp]==0:
            lst[tmp]=1
            fcnt+=1
            flag=1
            for j in dic[tmp]:
                f.append(j)
    
    for i in range(len(s)):
        tmp=s.popleft()
        if lst[tmp]==0:
            lst[tmp]=1
            scnt+=1
            flag=1
            for j in dic[tmp]:
                s.append(j)
    
    if flag==0:
        break
    

if fcnt>scnt:
    print("Fennec")
else:
    print("Snuke")