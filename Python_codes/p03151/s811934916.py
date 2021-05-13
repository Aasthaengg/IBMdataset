# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if sum(a) < sum(b):
        print(-1)
        return

    pos = []
    neg = 0
    for i in range(n):
        x = a[i] - b[i]
        if x >= 0:
            pos.append(x)
        else:
            neg += -x
    pos.sort(reverse=True)
    m = len(pos)
    i = 0
    cur = 0
    while i < m and cur < neg:
        cur += pos[i]
        i += 1
    print(n - len(pos) + i)
    


    
    
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

R s
S p
P r

"""
