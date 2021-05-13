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

n,k,c=map(int,input().split())
s=input()

l_lst=[0]*k
r_lst=[0]*k

l=-float('inf')
cnt=0
for i in range(n):
    if i-l>c and s[i]!="x":
        l_lst[cnt]=i
        cnt+=1
        l=i
        if cnt==k:
            break
# print(l_lst)
l=float('inf')
cnt=0
for i in range(n)[::-1]:
    if l-i>c and s[i]!="x":
        r_lst[-1-cnt]=i
        cnt+=1
        l=i
        if cnt==k:
            break
# print(r_lst)

for i,j in zip(l_lst,r_lst):
    if i==j:
        print(i+1)