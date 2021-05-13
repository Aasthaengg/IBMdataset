import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

s=input().rstrip()
n=len(s)
beki=[0 for i in range(n+1)]
beki[0]=1
for i in range(n):
    beki[i+1]=(beki[i]*10)%13

u=[[0 for i in range(13)] for j in range(n+1)]
u[0][0]=1
s=list(reversed(s))
for i in range(n):
    #z=i%3
    for j in range(13):
        if s[i]!="?":
            u[i+1][(j+beki[i]*int(s[i]))%13]+=u[i][j]%mod
        else:
            for k in range(10):
                u[i+1][(j+beki[i]*k)%13]+=u[i][j]%mod
#print(u)
print(u[n][5]%mod)