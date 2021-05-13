import sys
a, b, c = map(int,sys.stdin.readline().split())
d = c - a - b
if d > 0 and d * d > 4 * b * a:
  print("Yes")
else:
  print("No")