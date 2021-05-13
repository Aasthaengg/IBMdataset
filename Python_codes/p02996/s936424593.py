import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
a = [LIST() for i in range(n)]
a.sort(key=lambda x:x[1])
time = 0
for i in range(n):
        time += a[i][0]
        if(time>a[i][1]):
                print("No")
                exit()
print("Yes")