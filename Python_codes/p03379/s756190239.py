#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(readline())
X = list(map(int, readline().split()))
X_sorted = sorted(X)

# この二つ以外にありえない
small, large = X_sorted[(N-1)//2], X_sorted[(N+1)//2]

for x in X:
    if x <= small:
        print(large)
    else:
        print(small)