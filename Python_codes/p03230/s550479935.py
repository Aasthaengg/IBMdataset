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
tmp=int(math.sqrt(n*2))
if tmp*(tmp+1)!=n*2:
    print("No")
    exit()

lst=[]
cnt=1

for i in range(tmp+1):
    lsttmp=[len(lst)+1]
    for j in range(len(lst)):
        lsttmp.append(lst[j][lst[j][0]])
        lst[j][0]+=1
    # print(lst)
    # print(lsttmp)
    while len(lsttmp)<tmp+1:
        lsttmp.append(cnt)
        cnt+=1
    lst.append(lsttmp)
# print(lst)
print("Yes")
print(tmp+1)
for i in range(tmp+1):
    print(*([tmp]+lst[i][1:]))