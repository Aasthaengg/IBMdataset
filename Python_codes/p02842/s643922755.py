import math
n = int(input())
x = n/1.08
x1, x2 = math.floor( x ), math.ceil( x )

if n == math.floor( x1 * 1.08 ) :
  print(x1)
elif n == math.floor( x2 * 1.08 ):
  print(x2)
else:
  print(':(')