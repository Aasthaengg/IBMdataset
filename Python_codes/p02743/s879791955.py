ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

from math import sqrt

a,b,c=map(int, input().split())
if 4*a*b<(c-a-b)**2 and (c-a-b)>=0:
  print('Yes')
else:
  print('No')
