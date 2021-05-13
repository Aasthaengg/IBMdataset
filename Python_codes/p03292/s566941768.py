import sys
rl = lambda: list(map(int, sys.stdin.readline().split()))

a = sorted(rl())
print(a[2] - a[0])