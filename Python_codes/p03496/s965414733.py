# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n=I()
lis=LI()
mxabs=-1
pos=0
for i in range(n):
    if abs(lis[i])>mxabs:
        pos=i
        mxabs=abs(lis[i])
answers=[]
if lis[pos]>0:
    x=lis[pos]
    for i in range(n):
        if lis[i]<x:
            lis[i]+=x
            answers.append((pos+1,i+1))
    for i in range(n-1):
        if lis[i+1]<lis[i]:
            lis[i+1]+=lis[i]
            answers.append((i+1,i+2))
elif lis[pos]<0:
    x=lis[pos]
    for i in range(n):
        if lis[i]>x:
            lis[i]+=x
            answers.append((pos+1,i+1))
    for i in range(n-1):
        j=n-i-1
        if lis[j-1]>lis[j]:
            lis[j-1]+=lis[j]
            answers.append((j+1,j))
print(len(answers))
for i in range(len(answers)):
    print(*answers[i])
#print(lis)
    
    
