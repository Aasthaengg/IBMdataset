from math import sqrt
a,b=input().split()
c=int(a+b)
if sqrt(c)==int(sqrt(c)):
  print('Yes')
else:
  print('No')