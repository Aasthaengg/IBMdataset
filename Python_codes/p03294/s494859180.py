#!/usr/bin/env python3
import sys
import collections

sys.setrecursionlimit(10 ** 7)

# 1 ✕ 1 (int)
N = int(input().rstrip())

# 1 ✕ N
A = list(map(int, input().rstrip().split()))

print(sum(A) - N)
