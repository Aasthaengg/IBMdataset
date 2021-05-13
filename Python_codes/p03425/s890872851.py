# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    cc = ['M', 'A', 'R', 'C', 'H']
    cnt = defaultdict(int)
    for _ in range(n):
        s = input()
        if s[0] in cc:
            cnt[s[0]] += 1

    ans = 0
    from itertools import combinations
    kc = list(cnt.keys())
    for a, b, c in combinations(kc, 3):
        ans += cnt[a] * cnt[b] * cnt[c] 
    print(ans)
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""
