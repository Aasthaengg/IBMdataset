# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    x, y = [int(x) for x in input().split()]
    a, b = abs(x), abs(y)
    ans = abs(a - b)
    if x >= 0 and y > 0:
        if a > b:
            ans += 2
    elif x < 0 and y <= 0:
        if a < b:
            ans += 2
    else:
        ans += 1
    
    print(ans)



        
    

    
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""
