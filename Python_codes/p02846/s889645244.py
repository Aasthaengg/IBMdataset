import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

import math

t1,t2 = na()
a1,a2 = na()
b1,b2 = na()

p = a1*t1
q = b1*t1
x = p + a2*t2
y = q + b2*t2

if x < y:
  if p < q:
    print(0)
  elif p == q:
    print(1)
  elif p > q:
    print(int((p-q) / (y-x)) + math.ceil((p-q) / (y-x)))
elif x == y:
  print("infinity")
elif x > y:
  if p < q:
    print(int((q-p) / (x-y)) + math.ceil((q-p) / (x-y)))
  elif p == q:
    print(1)
  elif p > q:
    print(0)