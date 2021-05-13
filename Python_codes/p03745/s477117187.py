# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    p = 0
    for e in a:
        if p != e:
            b.append(e)
        p = e
    a = b
    n = len(b)

    ans = 0
    i = 0
    while i < n:
        ans += 1
        if i + 1 == n: break
        else:
            if a[i] < a[i+1]:
                while i + 1 < n and a[i] < a[i+1]:
                    i += 1
                i += 1
            else:
                while i + 1 < n and a[i] > a[i+1]:
                    i += 1
                i += 1
    print(ans)



    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
