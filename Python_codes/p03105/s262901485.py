a, b, c = list(map(int, input().split()))
n = b % a
if a * c <= b:
  print(c)
else:
  print(int((b - n) / a))