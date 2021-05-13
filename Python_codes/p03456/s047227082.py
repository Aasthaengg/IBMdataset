MM = input().split()
M1 = ''.join(MM)
M = int(M1)
import math
L =math.sqrt(M)
N = int(L)*int(L)
if N ==M:
  print('Yes')
else:
  print('No')