import math

n = int(input())

ans = math.ceil(n/1.08)

if n == int(ans*1.08):
  print(ans)
else:
  print(":(")