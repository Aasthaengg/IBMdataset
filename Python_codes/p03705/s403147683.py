n, a, b = map(int, input().split())
fst = (n - 1) * b + a
sec = (n - 1) * a + b
if a > b:
  print(0)
elif n == 1 and a != b:
  print(0)
else:
  print(fst - sec + 1)