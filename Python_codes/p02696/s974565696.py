import sys
input = sys.stdin.readline
from math import floor

A, B, N = map(int, input().split())

if N<B:
    print(floor(A/B*N))
else:
    print(floor(A/B*(B-1)))