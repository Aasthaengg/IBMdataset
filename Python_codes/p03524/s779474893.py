import bisect,copy,heapq,itertools,math,string
from collections import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')
if abs(a-b)<=1 and abs(b-c)<=1 and abs(c-a)<=1:
    print("YES")
else:
    print("NO")