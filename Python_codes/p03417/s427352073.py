n, m = map(int, input().split())

if n > 2 and m > 2:
  print((n-2)*(m-2))
elif n == 2 or m == 2:
  print(0)
elif n < 2 and m < 2:
  print(1)
else:
  print(max([0, m-2, n-2]))