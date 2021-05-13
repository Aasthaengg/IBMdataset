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
s = list(input() for i in range(n))
t = [0]*5

for i in range(n):
        if s[i][0] == 'M':
                t[0] += 1
        elif s[i][0] == 'A':
                t[1] += 1
        elif s[i][0] == 'R':
                t[2] += 1
        elif s[i][0] == 'C':
                t[3] += 1
        elif s[i][0] == 'H':
                t[4] += 1

c = combinations(range(5),3)
ans = 0   
for x in c:
        ans += t[x[0]] * t[x[1]] * t[x[2]]

print(ans)