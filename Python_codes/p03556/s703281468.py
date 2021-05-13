import math

n = int(input())

while True:
  x = math.sqrt(n)
  #####print(n)
  if x.is_integer():
    print(n)
    exit()
  n -= 1
