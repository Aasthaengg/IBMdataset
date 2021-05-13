# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    s = input()
    p = ''
    c = ''
    ans = 0
    for x in s:
        c += x
        if c == p:
            continue
        else:
            p = c
            c = ''
            ans += 1
    print(ans)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

a aa c ca c a b a ab a b c

"""
