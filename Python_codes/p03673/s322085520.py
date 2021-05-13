import bisect,copy,heapq,itertools,math,string
from collections import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
a = LIST()
b = deque()

for i in range(n):
    if(i%2==0):
        b.append(i)
    else:
        b.appendleft(i)

if(n%2==1):
    b.reverse()

c = [a[b[i]] for i in range(n)]
print(*c)