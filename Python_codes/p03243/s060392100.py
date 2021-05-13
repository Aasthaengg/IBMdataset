n = int(input())
if n % 100 <= n // 100 * 11:
  print(n // 100 * 111)
else:
  print((n // 100 + 1) * 111)