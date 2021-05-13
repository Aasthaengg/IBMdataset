import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
s = LIST()
count = 0
flag = 0
for i in range(n):
        if s[i] == i+1 and flag == 0:
                count += 1
                flag = 1
        else:
                flag = 0
        
print(count)