# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    a, b, c, d = [int(x) for x in input().split()]
    cd = c * d // gcd(c, d)
    x = ((b // c) - (a + c - 1) // c + 1)
    y = ((b // d) - (a + d - 1) // d + 1)
    z = ((b // cd) - (a + cd - 1) // cd + 1)
    print(b-a+1-(x+y-z))



        

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
