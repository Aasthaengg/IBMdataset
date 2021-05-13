import sys
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))

a, b = na()
print("error" if a+b >= 10 else a+b)