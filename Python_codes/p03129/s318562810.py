import math
 
a,b=map(int,input().split())
if math.ceil(a/2)>=b:
  print('YES')
else:
  print('NO')