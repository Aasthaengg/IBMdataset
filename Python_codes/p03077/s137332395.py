# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    ans = 0
    m = float('inf')
    for i in range(5):
        x = int(input())
        m = min(m, x)
    xd = (n + m - 1) // m
    print(xd + 4)



    




        
    

    
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

2 2 2 2 2

"""
