import sys

rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

a = sorted(rl(), reverse=True)
print(a[0]*10 + a[1] + a[2])