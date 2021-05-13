import sys

read = sys.stdin.read
readline = sys.stdin.readline

A, B, C = map(int, read().split())

if A == B == C:
    print('Yes')
else:
    print('No')
