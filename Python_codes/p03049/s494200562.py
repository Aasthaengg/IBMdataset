# -*- coding: utf-8 -*-
import sys
from collections import deque
from math import sqrt
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]

# n = int(input())



def solve():
    n = int(input())
    ans = 0
    a = 0
    b = 0
    c = 0
    for _ in range(n):
        s = input()
        a += s[-1] == 'A' and s[0] != 'B'
        b += s[0] == 'B' and s[-1] != 'A'
        c += s[0] == 'B' and s[-1] == 'A'
        ans += s.replace('AB', "*").count('*')
    if (a+b) > 0:
        print(ans + c + min(a, b))
    else:
        if c:
            c -= 1
        print(ans + c)
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()




"""




"""

