# -*- coding: utf-8 -*-
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

def set_distance(t, l, now, prev, pos):
    d = l[now][pos]

    for child in t[now]:
        if child == prev:
            continue
        l[child][pos] = d+1
        set_distance(t, l, child, now, pos)


n = int(input())
t = defaultdict(list)
for _ in range(n-1):
    a, b = map(lambda x: int(x) - 1, input().split())
    t[a].append(b)
    t[b].append(a)

# distance [fennec, snuke]
l = [[n, n] for _ in range(n)]
l[0][0] = 0
l[n-1][1] = 0

set_distance(t, l, 0, -1, 0)
set_distance(t, l, n-1, -1, 1)

f, s = 0, 0
for df, ds in l:
    if df <= ds:
        f += 1
    else:
        s += 1

if f > s:
    print('Fennec')
else:
    print('Snuke')
