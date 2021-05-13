import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
sys.setrecursionlimit(10 ** 6)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, m = MAP()
tmp = 1

for i in range(1,min(n,m)+1):
    tmp = tmp * i % (10**9+7)

if n == m:
    ans = tmp**2*2 % (10**9+7)
elif abs(n-m) == 1:
    ans = tmp**2*max(n,m) % (10**9+7)
else:
    ans = 0

print(ans)