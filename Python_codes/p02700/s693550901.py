A, B, C, D = map(int, input().split())
a = (A + D - 1) // D
c = (C + B - 1) // B
if c <= a:
  print('Yes')
else:
  print('No')