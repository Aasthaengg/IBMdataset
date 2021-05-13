a, b = list(map(int, input().split()))
if a + b < 24:
  print(a+b)
else:
  print((a+b) % 24)