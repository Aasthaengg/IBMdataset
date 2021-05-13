import math
N, X, T = map(int, input().split())
 
if N % X == 0:
  print(int(N / X * T))
else:
  print((math.floor(N/X) + 1) * T)