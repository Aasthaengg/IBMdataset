import sys, heapq, bisect, math, fractions
from collections import deque

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

res = 0
for i, a in enumerate(A):
    if i == A[a - 1] - 1 and i < a - 1:
        res += 1

print(res)