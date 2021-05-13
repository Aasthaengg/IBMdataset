# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase

def solve():
    s = input()
    a = [x for x in s]

    if s == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        return

    x = set(a)
    xd = []

    if len(s) == 26:
        while a[-2] > a[-1]:
            xd.append(a.pop())
        xd.append(a.pop())
        wtf = a.pop()
        xd.sort()
        for e in xd:
            if e > wtf:
                print(''.join(a) + e)
                return
    else:
        for e in string.ascii_lowercase:
            if e not in x:
                print(s + e)
                return
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
