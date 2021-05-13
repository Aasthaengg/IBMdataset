# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    cnt = defaultdict(int)
    for _ in range(n):
        s = [x for x in input()]
        s.sort()
        s = ''.join(s)
        cnt[s] += 1
    ans = 0
    for k in cnt:
        n = cnt[k]
        ans += n * (n - 1) // 2
    print(ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""
