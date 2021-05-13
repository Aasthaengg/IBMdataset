import math
import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split())

if (n - 1) * b + a - (n - 1) * a - b + 1 < 0:
    print(0)
else:
    print((n - 1) * b + a - (n - 1) * a - b + 1)