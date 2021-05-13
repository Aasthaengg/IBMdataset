from sys import stdin
import math
inp = lambda : stdin.readline().strip()

d, t, s = [int(x) for x in inp().split()]
if s*t >= d:
  print("Yes")
else:
  print("No")