#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
import re
 
s = input()
k = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
c = collections.Counter(s)

def nchars(s, n):
    """文字列 s に、同じ文字が n 個以上連続している部分文字列を見つける
    """
    assert n > 0
    reg = re.compile("(.)\\1{%d,}" % (n - 1))  # カンマを取ると n 個ちょうどになる
    while True:
        m = reg.search(s)
        if not m:
            break
        yield m.group(0)
        s = s[m.end():]

ans = 0

chains = list(nchars(s, 2))

if len(c) == 1:
    print(len(s) * k // 2)
else:
    #print(chains)
    #print(len(chains[0]), len(chains[-1]), k)
    for r in chains:
        ans += len(r) // 2

    if chains and chains[0] == chains[-1]:
        print(ans * k + (k - 1 if chains[0] == chains[-1] else 0))
    else:
        print(ans * k)
