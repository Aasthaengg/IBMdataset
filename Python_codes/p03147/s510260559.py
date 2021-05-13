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
    m = max(a)
    ans = 0
    for _ in range(m):
        b = a[:]
        for i in range(n):
            if a[i]:
                if i == 0 or a[i-1] == 0:
                    ans += 1
                b[i] -= 1
        a = b[:]

    print(ans)
        

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
