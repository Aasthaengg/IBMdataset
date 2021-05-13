import math
n = int(input())
d = 1
i = 1
while i <= math.sqrt(n):
  if n%i == 0:
    d = i
  i+=1
print(d + n//d -2)