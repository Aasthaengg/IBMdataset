import math

N = int(input())
raw = math.ceil(N / 1.08)
check = raw * 1.08

if int(check) == N:
  print(raw)
else :
  print(":(")
