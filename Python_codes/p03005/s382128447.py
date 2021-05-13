import sys
n, k = [int(i) for i in sys.stdin.readline().split()]
if k == 1:
  print(0)
else:
  print(n - k)