import math

N = int(input())
minimum = (-1,float('inf'))
for i in range(5):
  capa = int(input())
  if capa < minimum[1]:
    minimum = (i, capa)

print(math.ceil(N/minimum[1])+4)