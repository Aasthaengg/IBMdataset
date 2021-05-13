import sys

A, B, T = map(int, sys.stdin.readline().strip().split())
print(B * (T // A))