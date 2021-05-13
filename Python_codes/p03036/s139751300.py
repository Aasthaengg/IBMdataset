import math
import sys
input = sys.stdin.readline
X = [int(_) for _ in range(2500)]
r, d, x = map(int, input().split())
X[2000] = x
for i in range(2001, 2011):
    X[i] = r * X[i - 1] - d
[print(X[i]) for i in range(2001,2011)]