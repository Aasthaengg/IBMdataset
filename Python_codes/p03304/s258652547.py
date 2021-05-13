import sys
input = sys.stdin.readline
n, m, d = map(float, input().split())
t = float(n - d)
if d == 0: print((m - 1) * (1 / n))
else: print((m - 1) * 2 * t / pow(n, 2))