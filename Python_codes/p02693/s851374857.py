import math 

k = int(input())
a, b = map(int, input().split())

base = math.ceil(a / k)
if a <= k * base <= b:
  print('OK')
else:
  print('NG')