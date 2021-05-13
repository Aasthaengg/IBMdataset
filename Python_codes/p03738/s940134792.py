import math
A = math.log10(int(input()))
B = math.log10(int(input()))

if A > B:
  print('GREATER')
elif A < B:
  print('LESS')
else:
  print('EQUAL')