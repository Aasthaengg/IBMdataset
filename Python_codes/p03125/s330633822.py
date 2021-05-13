A, B = map(int, input().split())

if (B / A).is_integer():
  print(B + A)
else:
  print(B - A)