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
    # n, m = [int(x) for x in input().split()]
    s = [x for x in input()]
    k = int(input())
    n = len(s)
    if len(set(s)) == 1:
        print(n*k//2)
        return
    b = [1]
    for i in range(1, n):
        if s[i] == s[i-1]:
            b[-1] += 1
        else:
            b.append(1)
    ans = 0
    for e in b:
        ans += e // 2 * k

    if s[0] == s[-1] and b[0] % 2 and b[-1] % 2:
        ans += k-1
    
    print(ans)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
