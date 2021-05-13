a, b, c, d = (int(x) for x in input().split())
if abs(a - c) <= d or (abs(a-b) <=d and abs(b-c) <= d):
  print('Yes')
else:
  print('No')