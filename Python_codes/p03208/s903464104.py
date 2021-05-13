# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, k = [int(x) for x in input().split()]
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    ans = float('inf')
    for i in range(n-k+1):
        ans = min(ans, a[i+k-1]-a[i])
    print(ans)
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

a aa c ca c a b a ab a b c

"""
