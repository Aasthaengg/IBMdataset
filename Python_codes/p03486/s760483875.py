# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    s = [x for x in input()]
    t = [x for x in input()]
    s.sort()
    t.sort(reverse=True)
    if s < t:
        print("Yes")
    else:
        print("No")



    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
