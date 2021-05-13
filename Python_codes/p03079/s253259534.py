import sys
l = sys.stdin.readline().strip().split()
a, b, c = [int(x) for x in l]
if (a == b) & (b == c):
  print('Yes')
else:
  print('No')