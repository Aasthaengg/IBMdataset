import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

import math

k = ni()
a = na()

r,l = 2,2

for i in a[::-1]:
    if r < i:
        print(-1)
        exit()
    l = math.ceil(l/i)*i
    r = (r//i)*i+i-1
    if l > r:
        print(-1)
        exit()

print(l,r)