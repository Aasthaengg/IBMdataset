import math
a,b=map(int,input().split())
if b < 10:
  a *= 10
elif b <100:
  a *= 100
else:
  a *=1000
a_b =a + b
if math.sqrt(a_b) - int(math.sqrt(a_b)) == 0:
  print('Yes')
else:
  print('No')