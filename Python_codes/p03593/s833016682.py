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

h,w=map(int,input().split())
a=[input() for i in range(h)]

lst=[0]*26
for i in range(h):
    for j in range(w):
        lst[ord(a[i][j])-ord("a")]-=1

# print(lst)

heapq.heapify(lst)
dic=defaultdict(int)
if h%2==0:
    if w%2==0:
        dic[4]=h*w//4
    else:
        dic[4]=(w-1)*h//4
        dic[2]=h//2
else:
    if w%2==0:
        dic[4]=(h-1)*w//4
        dic[2]=w//2
    else:
        dic[4]=(h-1)*(w-1)//4
        dic[2]=h//2+w//2
        dic[1]=1
# print(dic)
# print(lst)
for i in range(dic[4]):
    tmp=-heapq.heappop(lst)
    if tmp>=4:
        tmp-=4
        heapq.heappush(lst,-tmp)
    else:
        print("No")
        quit()

for i in range(dic[2]):
    tmp=-heapq.heappop(lst)
    if tmp>=2:
        tmp-=2
        heapq.heappush(lst,-tmp)
    else:
        print("No")
        quit()

for i in range(dic[1]):
    tmp=-heapq.heappop(lst)
    if tmp>=1:
        tmp-=1
        heapq.heappush(lst,-tmp)
    else:
        print("No")
        quit()
# print(lst)
print("Yes")