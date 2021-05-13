import math

N = int(input())

K = math.ceil((-1 + math.sqrt(1 + 8 * N))/2)

L = int((1 + K) * K //2 - N)

while K:
  if K != L:
    print(K)
  K -= 1