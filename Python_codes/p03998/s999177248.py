# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    a = input()
    b = input()
    c = input()
    i = 0
    j = 0
    k = 0
    t = 'a'
    while 1:
        if t == 'a':
            if i == len(a):
                print('A')
                return
            t = a[i]
            i += 1
        elif t == 'b':
            if j == len(b):
                print('B')
                return
            t = b[j]
            j += 1
        else:
            if k == len(c):
                print('C')
                return
            t = c[k]
            k += 1
        
    
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
