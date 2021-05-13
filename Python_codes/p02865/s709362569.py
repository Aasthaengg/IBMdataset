from math import floor

N = int(input())

if N % 2 == 0:
  print(round(N / 2 - 1))
else:
  print(floor(N / 2))