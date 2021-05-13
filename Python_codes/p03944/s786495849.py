import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

w, h, n = MAP()
a = [LIST() for i in range(n)]
x0 = 0
x1 = w
y0 = 0
y1 = h

for i in range(n):
        if a[i][2] == 1:
                x0 = max(x0, a[i][0])
        elif a[i][2] == 2:
                x1 = min(x1, a[i][0])
        elif a[i][2] == 3:
                y0 = max(y0, a[i][1])
        elif a[i][2] == 4:
                y1 = min(y1, a[i][1])

print(max(0, y1-y0)*max(0, x1-x0))