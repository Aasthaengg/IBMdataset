import math

A, B = map(int, input().split())

x = math.ceil(100 / 8 * A)
y = math.ceil(100 / 10 * B)

if x == y:
  print(x)
elif x > y:
  if math.floor(x*0.1) == B:
    print(x)
  else:
    print(-1)
else:
  if math.floor(y*0.08) == A:
    print(y)
  else:
    print(-1)