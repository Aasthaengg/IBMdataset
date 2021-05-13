# -*= coding: utf-8 -*-

N, A, B = map(int, input().split())
if A == 0:
  print(0)
  exit()
x = N // (A+B)
x = x * A

y = N % (A+B)
if y >= A:
  y = A

print(x + y)