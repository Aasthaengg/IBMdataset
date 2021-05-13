# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


def solve():
    # n, m = [int(x) for x in input().split()]
    n = int(input())
    s = input()
    cnt = defaultdict(int)
    for e in s:
        cnt[e] += 1
    ans = 0
    for i in range(n):
        e = s[i]
        x = n - i - cnt[e]
        xd = 1
        cnt[e] -= 1
        for c in cnt:
            if cnt[c] and c != e:
                xd *= (cnt[c]+1)
        ans += xd
        ans %= MOD
    
    print(ans%MOD)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
