import sys
a, b = map(int, sys.stdin.readline().split())
if a <= b*2:
  print(0)
else:
  print(a - b*2)