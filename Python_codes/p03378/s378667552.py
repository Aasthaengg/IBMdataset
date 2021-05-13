#!/usr/bin/env python3

N,M,X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

B = [0] * (N+1)

for a in A:
    B[a] = 1

print(min(B[:X].count(1), B[X+1:].count(1)))
