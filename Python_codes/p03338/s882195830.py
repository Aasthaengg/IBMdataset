# -*- coding: utf-8 -*-
import sys
from collections import defaultdict, deque
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]


def solve():
    n = int(input())
    s = [x for x in input()]
    ans = 0
    for i in range(n - 1):
        a = set(s[:i+1])
        b = set(s[i+1:])
        ans = max(ans, len(a & b))
    print(ans)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()

"""

"""

