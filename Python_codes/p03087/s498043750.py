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

n, q = MAP()
s = input()
p = [LIST() for i in range(q)]
l = [0]*n
r = [0]*n

for i in range(n-1):
    if s[i] + s[i+1] == "AC":
        l[i] += 1
        r[i+1] += 1

for i in range(1,n):
    l[i] += l[i-1]
    r[i] += r[i-1]

for i in range(q):
    print( r[p[i][1]-1] - r[p[i][0]-1] )