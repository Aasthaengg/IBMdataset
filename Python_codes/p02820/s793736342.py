#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

X = [[] for _ in range(K)]

for i in range(N):
    X[i % K].append(T[i])

pt = {'r': P, 's': R, 'p': S}

score = 0
for k in range(K):
    last = None
    for st in X[k]:
        if st != last:
            score += pt[st]
            last = st
        else:
            last = None

print(score)

