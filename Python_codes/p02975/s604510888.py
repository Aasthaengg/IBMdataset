N = int(input())
A = [int(i) for i in input().split()] 

from functools import reduce
from operator import xor
ans = reduce(xor, A)

if ans == 0:
  print('Yes')
else:
  print('No')