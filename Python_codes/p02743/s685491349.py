import math
import numpy
a,b,c=map(int,input().split())
if 4*a*b<pow(c-a-b,2) and c-a-b>0:
  print('Yes')
else:
  print('No')