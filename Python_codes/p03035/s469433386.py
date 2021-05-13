import sys
A, B = map(int, sys.stdin.readline().split())

if A >= 13:
  print(B)
if 6 <= A <= 12:
  print(int(B / 2))
if A < 6:
  print(0)