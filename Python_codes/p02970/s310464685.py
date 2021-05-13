# import sys
# sys.setrecursionlimit(10**5)
# from collections import defaultdict

geta = lambda fn: list(map(fn, input().split()))
gete = lambda fn: fn(input())

n, d = geta(int)
print((n + 2 * d) // (2 * d + 1))
