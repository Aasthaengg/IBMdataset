import math

H, W = map(int, input().split(' '))

if H == 1 or W == 1:
  print(1)
else:
  print(int((H*W+1)/2))
