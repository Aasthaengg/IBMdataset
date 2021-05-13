from sys import stdin
a, b, c = [int(x) for x in stdin.readline().rstrip().split()]
if c >= a and c <= b:
  print('Yes')
else:
  print('No')