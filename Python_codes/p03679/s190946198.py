import sys
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))

x, a, b = na()
if a >= b:
    print("delicious")
elif (a+x) >= b:
    print("safe")
else:
    print("dangerous")
