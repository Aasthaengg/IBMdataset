import sys
stdin = sys.stdin
from itertools import product

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))

r = ni()
g = ni()
print(g + (g-r))