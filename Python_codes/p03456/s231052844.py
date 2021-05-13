import math
a, b = [str(x) for x in input().split()]
ab = int(a+b)
ab = math.sqrt(ab)
if(ab.is_integer()):
  print('Yes')
else:
  print('No')
