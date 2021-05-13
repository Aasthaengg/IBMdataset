import sys

N, M = map(int, sys.stdin.readline().split())
print(2 ** M * (1900 * M + 100 * (N - M)))