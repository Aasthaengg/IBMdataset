import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, m = MAP()
s = input()
t = input()
k = gcd(n,m)
l = n*m//k

for i in range(0,l,l//k):
        if (n*i) % l == (m*i) % l == 0 and s[n*i//l] != t[m*i//l]:
                print(-1)
                exit()
print(l)