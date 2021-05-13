# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    d = defaultdict(int)
    a = [int(x) for x in input().split()]
    for e in a:
        d[e] += 1
    m = int(input())
    t = [int(x) for x in input().split()]
    for e in t:
        if d[e]:
            d[e] -= 1
        else:
            print("NO")
            return
    print("YES")
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""
