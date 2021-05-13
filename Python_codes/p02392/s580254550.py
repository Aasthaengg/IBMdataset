#! python3

a, b, c = [int(x) for x in input().strip().split(' ')]
if a < b < c:
  print('Yes')
else:
  print('No')