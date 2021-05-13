n, b, r = map(int, input().split())

total = b + r
num = n // total
rest = n - (num * total)

if rest <= b:
  print(num * b + rest)
else:
  print(num * b + b)