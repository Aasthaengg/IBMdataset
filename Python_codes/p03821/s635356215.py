import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
a = [LIST() for i in range(n)]
ans = 0

for x in a[::-1]:
        if ( x[0] + ans ) % x[1] != 0:
                ans += x[1] - ( x[0] + ans ) % x[1]
print(ans)