import math
a,b=list(map(str,input().split()))
txt=int(a+b)

a=int(math.sqrt(txt))
if txt==a*a:
  print('Yes')
else:
  print('No')