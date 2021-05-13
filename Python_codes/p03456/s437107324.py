from math import sqrt
a, b = map(int, input().split())
i = 1
while i <= b:
  i *= 10
  a *= 10
X = a + b
if int(sqrt(X)) ** 2 == X:
  print("Yes")
else:
  print("No")