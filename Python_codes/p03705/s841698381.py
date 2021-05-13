import sys

N, A, B = map(int, input().split())

mi = A * (N-1) + B
ma = A + B * (N-1)

if ma - mi + 1 < 0:
  print(0)
  sys.exit()

print(ma - mi + 1)