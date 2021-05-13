#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

N = int(input())
P = []
for i in range(N):
   P.append(int(input()))


P.sort()
#print(P)

res = sum(P[:-1]) + P[-1]//2

print(res)
