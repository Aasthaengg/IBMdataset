from math import sqrt
N = int(input())
for i in range(N, 0, -1):
  if sqrt(i).is_integer():
    print(i)
    exit()