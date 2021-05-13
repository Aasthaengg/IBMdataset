a,b,c = [int(i) for i in input().split()]

import math

root_a = math.sqrt(a)
root_b = math.sqrt(b)
root_c = math.sqrt(c)

if 4*a*b< (c - b -a)**2 and c - a - b >0:
  print('Yes')
else:
  print('No')