# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


def solve():
    # n, m = [int(x) for x in input().split()]  
    n, q = [int(x) for x in input().split()]  
    g = defaultdict(list)
    cnt = [0] * (n+1)

    for _ in range(n-1):
        a, b = [int(x) for x in input().split()]  
        g[a].append(b)
        g[b].append(a)

    for _ in range(q):
        v, x = [int(x) for x in input().split()]
        cnt[v] += x
    
    q = deque([(1, 0)])
    w = set([1])
    while q:
        v, val = q.popleft()
        cnt[v] += val
        for to in g[v]:
            if to not in w:
                q.append((to, cnt[v]))
                w.add(to)

    print(*cnt[1:])


    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
a b a
d c d
a b a
"""
