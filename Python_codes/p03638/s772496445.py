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

h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
lst=[[0]*w for i in range(h)]
# yoko=[0,w-1]
# tate=[0,h-1]
now=[0,0]
muki=0
# print(lst)
def chech(x,y):
    if 0<=x<w and 0<=y<h:
        if lst[y][x]==0:
            return 1
        else:
            return 0
    else:
        return 0

while a:
    lst[now[1]][now[0]]=len(a)
    a[-1]-=1
    if a[-1]==0:
        a.pop()
    # print(a)
    # print(lst)
    # print(now)
    if muki==0:
        if chech(now[0]+1,now[1]):
            now[0]+=1
        else:
            if chech(now[0],now[1]+1):
                now[1]+=1
                muki=1
            else:
                break
    elif muki==1:
        if chech(now[0],now[1]+1):
            now[1]+=1
        else:
            if chech(now[0]-1,now[1]):
                now[0]-=1
                muki=2
            else:
                break
    elif muki==2:
        if chech(now[0]-1,now[1]):
            now[0]-=1
        else:
            if chech(now[0],now[1]-1):
                now[1]-=1
                muki=3
            else:
                break
    elif muki==3:
        if chech(now[0],now[1]-1):
            now[1]-=1
        else:
            if chech(now[0]+1,now[1]):
                now[0]+=1
                muki=0
            else:
                break
for i in range(h):
    print(*lst[i])