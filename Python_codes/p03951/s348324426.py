# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    s = input()
    t = input()
    for i in range(n, 0, -1):
        x = s[-i:]
        y = t[:i]
        if x == y:
            print(len(s[:n-i] + t))
            return
    print(n*2)


    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
