import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
amari=[0]*k
for i in range(n):
    i+=1
    amari[i%k]+=1
# print(amari)

ans=0
for i in range(n):
    i+=1
    am=i%k
    nokori=(k-am)%k
    # print(am,nokori)
    if nokori*2%k==0:
        ans+=amari[nokori]**2
print(ans)