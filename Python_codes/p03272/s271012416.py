import sys
stdin = sys.stdin

na = lambda: list(map(int, stdin.readline().split()))
n, i = na()

print(n - i + 1)