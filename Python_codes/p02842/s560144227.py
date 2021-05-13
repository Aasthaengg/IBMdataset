import math
N = int(input())
S = math.ceil(N / 1.08)
if S * 1.08 <= N - 1 or S * 1.08 >= N + 1:
  print(":(")
else:
  print(S)
