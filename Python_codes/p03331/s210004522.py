n = int(input())
if n % 10 == 0:
  print(10)
else:
  result = sum(list(map(int, str(n))))
  print(result)