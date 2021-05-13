import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, p = MAP()
a = list(map(lambda x:int(x)%2, input().split()))
e = a.count(0) if 0 in a else 0
o = a.count(1) if 1 in a else 0

ans = 0
if(p == 0):
    for i in range(0,e+1):
        for j in range(0,o+1,2):
            comb_e = factorial(e)//factorial(i)//factorial(e-i)
            comb_o = factorial(o)//factorial(j)//factorial(o-j)
            ans += comb_e * comb_o
else:
    for i in range(0,e+1):
        for j in range(1,o+1,2):
            comb_e = factorial(e)//factorial(i)//factorial(e-i)
            comb_o = factorial(o)//factorial(j)//factorial(o-j)
            ans += comb_e * comb_o
print(ans)