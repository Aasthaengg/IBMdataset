# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, q = [int(x) for x in input().split()]
    s = input()
    a = [0] * n
    b = [0] * n
    for i in range(n-1):
        if s[i:i+2] == 'AC':
            a[i] = 1
        b[i] = a[i]
        if i:
            b[i] += b[i-1]
    for _ in range(q):
        l, r = [int(x) for x in input().split()]
        l -= 1
        r -= 1
        ans = b[r-1]
        if l:
            ans -= b[l-1]
        print(ans)
    
    

        
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

R s
S p
P r

"""
