#!/usr/bin/env python

n = int(input())

tScore = 0
hScore = 0

for i in range(n):
    T, H = input().split()
    if T == H:
        tScore += 1
        hScore += 1
    elif T > H:
        tScore += 3
    elif H > T:
        hScore +=3
print("%d %d" % (tScore, hScore))