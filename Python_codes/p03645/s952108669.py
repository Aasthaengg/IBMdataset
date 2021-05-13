# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, m = [int(x) for x in input().split()]
    g = defaultdict(set)
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        g[a].add(b)
        g[b].add(a)
    
    for i in range(2, n):
        if 1 in g[i] and n in g[i]:
            print("POSSIBLE")
            return
    print("IMPOSSIBLE")



t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""
