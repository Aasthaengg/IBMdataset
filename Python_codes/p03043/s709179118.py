# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, k = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n + 1):
        x = 1 / n
        score = i
        while score < k:
            score *= 2
            x /= 2
        ans += x
    print(ans)


    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""
