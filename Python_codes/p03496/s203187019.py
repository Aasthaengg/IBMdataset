#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007


#A
def A():
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    n = I()
    a = LI()
    if sorted(a) == a:
        print(0)
        quit()
    ans = []
    ma = a.index(max(a))
    mi = a.index(min(a))
    if a[ma] > abs(a[mi]):
        if ma != 0:
            for i in range(2):
                ans.append([ma+1,1])
        for i in range(n-1):
            for j in range(2):
                ans.append([i+1,i+2])
    else:
        if mi != n-1:
            for i in range(2):
                ans.append([mi+1,n])
        for i in range(n-1)[::-1]:
            for j in range(2):
                ans.append([i+2,i+1])
    print(len(ans))
    for i,j in ans:
        print(i,j)
#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    D()
