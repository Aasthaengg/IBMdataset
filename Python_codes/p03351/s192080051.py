import sys
a,b,c,d = [int(num) for num in input().split()]
a_b = abs(b - a)
b_c = abs(c - b)
a_c = abs(a - c)

if a_c <= d:
  print('Yes')
  sys.exit(0)
if a_b <= d and b_c <= d: 
  print('Yes')
  sys.exit(0)
else:
  print('No')