import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

a,b,n = na()

if b-1 < n:
  c = b-1
  print(a*c//b-a*(c//b))
else:
  print(a*n//b-a*(n//b))