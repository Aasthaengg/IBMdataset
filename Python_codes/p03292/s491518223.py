import sys
rl = lambda: list(map(int, sys.stdin.readline().split()))

a = rl()
print(max(a) - min(a))