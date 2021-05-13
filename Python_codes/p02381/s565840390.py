import math
while True:
  n = int(input())
  if n == 0:
    break
  s = [int(_) for _ in input().split()]
  m = sum(s)/n
  a = math.sqrt( sum([pow(_-m, 2) for _ in s])/n )
  print(a)