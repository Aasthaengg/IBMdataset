import sys
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
s = lambda h: [list(map(int, stdin.readline().split())) for i in range(h)]

a, b, c = na()

print("YES" if b - a == c - b else "NO")