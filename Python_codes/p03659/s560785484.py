# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    sm = sum(a)
    xd = 0
    ans = float('inf')
    for i in range(n-1):
        xd += a[i]
        sm -= a[i]
        ans = min(ans, abs(xd - sm))
    print(ans)

        
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

7
3 1
4 1
5 9
2 6
5 3
5 8
9 7 5

"""
