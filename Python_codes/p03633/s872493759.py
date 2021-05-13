# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')

def lcm(x, y):
    return x * y // gcd(x, y)
def solve():
    n = int(input())
    ans = 0
    for i in range(n):
        t = int(input())
        if i:
            ans = lcm(ans, t)
        else:
            ans = t
    print(ans)
    

        
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

7
3 1
4 1
5 9
2 6
5 3
5 8
9 7 5

"""
