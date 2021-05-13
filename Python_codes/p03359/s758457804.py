import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

a, b = na()
if a <= b:
    print(a)
else:
    print(a-1)