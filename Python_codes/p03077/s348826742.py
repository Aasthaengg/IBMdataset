import math

L = []
for _ in range(6):
  L.append(int(input()))

print(4 + math.ceil(L[0]/min(L[1:])))