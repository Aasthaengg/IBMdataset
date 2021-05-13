# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, m = [int(x) for x in input().split()]
    d = defaultdict(list)
    for _ in range(m):
        s, c = [int(x) for x in input().split()]
        s -= 1
        d[s].append(c)
    ans = ''
    for i in range(n):
        x = int(n > 1)
        if i:
            x = 0
        
        if len(set(d[i])) > 1:
            print(-1)
            return
        elif d[i]:
            x = d[i][0]
        ans += str(x)

    if n != 1 and ans[0] == '0':
        print(-1)
    else:
        print(ans)



    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""
