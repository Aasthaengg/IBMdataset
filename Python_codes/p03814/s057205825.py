# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    s = input()
    a = []
    z = []
    for i, c in enumerate(s):
        if c == 'A':
            a.append(i)
        if c == 'Z':
            z.append(i)
    
    print(z[-1]-a[0]+1)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()




"""

4
1 2
2 4
1 3
3
2 2 4
4 5 6

6
1 2
2 3
3 4
4 5
4 6
3
3 5 6
2 17 31 5 11

"""



