# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


def solve():
    # n, m = [int(x) for x in input().split()]
    n, m = [int(x) for x in input().split()]
    s = []
    for _ in range(m):
        k, *r = [int(x) - 1 for x in input().split()]
        s.append(r)
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(2 ** n): # mask
        ok = 1
        for j in range(m): # bulb
            pp = p[j]
            cnt = 0
            for ss in s[j]:
                if i & (1 << ss):
                    cnt += 1
            if cnt % 2 != pp:
                ok = 0
        ans += ok
    print(ans)

    


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
