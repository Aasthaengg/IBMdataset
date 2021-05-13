import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())

import collections
d = collections.defaultdict(list)

for i in range(N):
    S, P = input().split()
    P = int(P)
    d[S].append((i+1, P))

ordered = list(d.keys())
ordered.sort()

for city in ordered:
    mises = d[city]
    mises = sorted(mises, key=lambda x: x[1], reverse=True)
    for mise in mises:
        print(mise[0])