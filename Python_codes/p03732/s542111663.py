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

n,W=map(int,input().split())
wv=[list(map(int,input().split())) for i in range(n)]

w1=wv[0][0]
wv.sort()
lst=[[],[],[],[]]
for i in range(n):
    w,v=wv[i]
    lst[w-w1].append(v)
# print(lst)
ruilst=[]
for i in range(4):
    ruilst.append(ruiseki(lst[i][::-1]))
# print(ruilst)

ans=0
for i in range(len(ruilst[0])):
    for j in range(len(ruilst[1])):
        for k in range(len(ruilst[2])):
            for l in range(len(ruilst[3])):
                if i*w1+j*(w1+1)+k*(w1+2)+l*(w1+3)<=W:
                    ans=max(ans,ruilst[0][i]+ruilst[1][j]+ruilst[2][k]+ruilst[3][l])
print(ans)