n, m = map(int, input().split())

if n == 1 and m == 1:
  print(1)
else:
  print(abs((n-2)*(m-2)))