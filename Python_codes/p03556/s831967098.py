import math
N =int(input())

for i in range(N,0,-1):
  x = math.sqrt(i)
  if x.is_integer():
    print(i)
    exit()