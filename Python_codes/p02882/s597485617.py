import sys
readline = sys.stdin.readline

A,B,X = map(int,readline().split())

bottle = (A ** 2) * B
x = -1
y = -1
import math
area = X / A
if X < bottle / 2:
  y = (X * 2 / B) / A
  x = B
  print(90 - math.degrees(math.atan(y/x)))
else:
  x = (bottle - X) * 2 / (A ** 2)
  y = A
  if x == 0:
    print(0)
  else:
    print(90 - math.degrees(math.atan(y/x)))
