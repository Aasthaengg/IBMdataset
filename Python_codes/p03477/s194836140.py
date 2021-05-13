import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

a,b,c,d = na()
e = a+b
f = c+d

print('Left' if e > f else 'Balanced' if e == f else 'Right')