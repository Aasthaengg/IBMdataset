import math

N = int(input())

X = N/1.08

if (X % 1 == 0):
  print(int(X))
elif (math.floor(math.ceil(X) * 1.08) == N):
  print(math.ceil(X))
else:
  print(":(")