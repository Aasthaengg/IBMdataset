from math import ceil
n,a,b = map(int,input().split())
d = b-a
if d%2==0:
  print(d//2)
else:
  print(min(n-b,a-1) + (b-a)//2 + 1)