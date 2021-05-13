L = list(sorted(map(int, input().split())))
if L[0] % 2 == 0 or L[1] % 2 == 0 or L[2] % 2 == 0:
  print(0)
else:
  print(L[0] * L[1])