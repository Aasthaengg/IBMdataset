import math
a,b,x = map(int,input().split())

if b >= 0:
  bb = b//x+1
else:
  bb = 0
  
if a >= 0:
  a = a - 1
  aa = a//x+1
else:
  aa = 0
print(bb-aa)
