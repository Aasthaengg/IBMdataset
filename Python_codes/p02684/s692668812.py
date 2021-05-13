#!/usr/bin/env python3

import sys
from collections import defaultdict
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, K = map(int, readline().split())
A = list(map(int, readline().split()))
A = [a-1 for a in A]


seen = defaultdict(list)
count = 0
pos = 0
seen[pos].append(count)

while True:
    pos = A[pos]
    count += 1
    seen[pos].append(count)
    if len(seen[pos]) == 2:
        head = seen[pos][0]
        loop = count - head
        break


if K < head:
    pos = 0
    for i in range(K):
        pos = A[pos]
    print(pos+1)


else:
    K = K - head
    res = K % loop
    for i in range(res):
        pos = A[pos]

    print(pos+1)


