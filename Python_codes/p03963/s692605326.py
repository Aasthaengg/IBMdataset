import sys

N, K = map(int, sys.stdin.readline().split())
print(K * (K - 1) ** (N - 1))