import math
N, M = [int(i) for i in input().split()]
for i in range(M//N, 0, -1):
  if M % i == 0:
    print(i)
    break
