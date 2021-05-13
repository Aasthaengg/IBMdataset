n, m, d = map(int, input().split())

if d == 0:
  result = (m - 1) / n
else:
  result = ( n - d ) * 2 * (m - 1) / n / n

if result > 0.0000001:
  print(result)
else:
  print("0.000000")