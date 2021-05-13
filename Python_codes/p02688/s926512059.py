#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__


N, K = map(int, input().split())

S = set(list(range(1, N+1)))
for k in range(K):
   d = int(input())
   A = list(map(int, input().split()))
   for x in A:
      if x in S:
         S.remove(x)

print(len(S))


