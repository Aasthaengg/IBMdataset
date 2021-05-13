import sys

X, A = map(int, sys.stdin.readline().strip().split())
print(0 if X < A else 10)