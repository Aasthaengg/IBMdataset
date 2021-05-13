# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left

def solve():
    n = int(input())
    ans = [0] * n
    a = [int(x) for x in input().split()]
    ok = 1
    cur = n - 1
    while ok and a:
        ok = 0
        i = len(a) - 1
        while i >= 0:
            if a[i] - 1 == i:
                ok = a[i]
                a.pop(i)
                break
            i -= 1
        ans[cur] = ok
        cur -= 1

    if a:
        print(-1)
    else:
        for e in ans:
            print(e)
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
