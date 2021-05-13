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

m,k=map(int,input().split())

if m==0 and k!=0:
    print(-1)
    quit()
elif m==1 and k!=0:
    print(-1)
    quit()
elif k>=2**m:
    print(-1)
    quit()
if m==1 and k==0:
    print(*[0,0,1,1])
    quit()

lst=[i for i in range(2**m) if i!=k]
# print(lst)
anslst=lst[:]+[k]+sorted(lst,key=lambda x: -x)+[k]
print(*anslst)