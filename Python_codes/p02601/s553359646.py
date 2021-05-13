from math import log2
from math import ceil
a,b,c = map(int,input().split())
k = int(input())
s1 = max(ceil(log2((a+1)/b)),0)
s2 = max(ceil(log2((b*2**s1+1)/c)),0)
if s1+s2 <= k:
  print('Yes')
else:
  print('No')
