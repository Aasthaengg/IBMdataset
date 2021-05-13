a, b, c = list(map(int, input().split()))
if a <= c <= a + b:
  print('YES')
else:
  print('NO')