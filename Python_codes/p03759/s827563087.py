from sys import stdin
a, b, c = [int(x) for x in stdin.readline().rstrip().split()]
if (b-a) == (c-b):
  print('YES')
else:
  print('NO')