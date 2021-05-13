# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, k = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    a = [(x+1)*x//2/x for x in p]
    ans = 0
    sm = 0
    for i in range(n):
        sm += a[i]
        if i + 1 >= k:
            ans = max(ans, sm)
            sm -= a[i - k + 1]
    print(ans)



    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""
