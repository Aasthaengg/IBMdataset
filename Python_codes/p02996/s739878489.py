# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    d = []
    for _ in range(n):
        f, s = [int(x) for x in input().split()]
        d.append((s, f))
    d.sort()
    cur = 0
    for b, a in d:
        cur += a
        if cur > b:
            print("No")
            return
    print("Yes")


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
