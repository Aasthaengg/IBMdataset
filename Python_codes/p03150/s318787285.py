# -*- coding: utf-8 -*-
import sys
from collections import defaultdict, deque
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]


def solve():
    s = input()
    t = 'keyence'
    n = len(s)
    
    for i in range(n):
        for j in range(n - i):
            x = (s[:i] + s[i+j:])
            if x == t:
                print("YES")
                return



    print("NO")


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()

"""

"""

