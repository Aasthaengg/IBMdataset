import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

a, b, c = MAP()
print("Yes" if c-a-b > 0 and a**2+b**2+c**2-2*(a*b+b*c+c*a) > 0 else "No")