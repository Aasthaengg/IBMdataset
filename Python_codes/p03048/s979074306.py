# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    a,b,c,n = [int(x) for x in input().split()]
    cnt = 0
    for i in range(0,n+1,a):
        for j in range(0,n+1,b):
            if i + j == n or (
                i + j < n and (
                    (n - (i + j)) % c == 0
                )):
                cnt += 1
    print(cnt)


    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""
