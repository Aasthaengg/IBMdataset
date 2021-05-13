import math

x = int(input())
ans = 0

while ans == 0:
  for i in range(2,math.floor(math.sqrt(x))+1):
    if x % i == 0:
      break
  else:
    ans = x
  x += 1

print(ans)