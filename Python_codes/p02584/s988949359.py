import math

value = input().split()
X = int(value[0])
K = int(value[1])
D = int(value[2])

if X != 0:
  if X < 0:
    X = -X
  if K * D <= X:
    print(X - K * D)
  else:
    R = math.ceil(X / D)
    K -= R
    X -= D * R
    if K % 2 == 0:
      print(-X)
    else:
      print(X + D)  
else:
  if K % 2 == 0:
    print("0")
  else:
    print(D)