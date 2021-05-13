# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, a, b, c, d = [int(x) for x in input().split()]
    s = input() + '#'
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    
    gg = 0
    y = s.find('##', a)
    if y != -1 and y <= max(c, d) and y > min(a, b):
        gg = 1
    if c > d:
        x = s.find('...', b)
        xd = 1
        if ((s[b + 1] == s[b - 1] and s[b - 1] == '.') 
            or (s[b+1] == s[b+2]  and s[b+1] == '.')
            or (x != -1 and x + 1 <= d)):
            xd = 0
        if gg or xd:
            print("No")
        else:
            print("Yes")
    else:
        if gg:
            print("No")
        else:
            print("Yes")

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""
