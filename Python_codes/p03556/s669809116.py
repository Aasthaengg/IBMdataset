import math
N=int(input())

while True:
  if math.sqrt(N).is_integer():
    print(N)
    break
  N-=1