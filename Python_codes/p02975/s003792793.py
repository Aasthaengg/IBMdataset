# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = defaultdict(int)
    for e in a:
        d[e] += 1
    ks = list(d.keys())
    m = len(ks)
    if m < 4:
        x = n / 3
        if m == 1 and ks[0] == 0:
            print("Yes")
            return
        elif m == 2:
            if d[0] == x:
                print("Yes")
                return
        elif m == 3:
            a, b, c = ks
            if d[a] == d[b] and d[a] == d[c] and (a^b^c) == 0:
                print("Yes")
                return
    
    print("No")


    


    
    
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

R s
S p
P r

"""
