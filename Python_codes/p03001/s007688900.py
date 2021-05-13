import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

w,h,x,y = MAP()
print(w*h/2, 1 if x==w/2 and y==h/2 else 0)