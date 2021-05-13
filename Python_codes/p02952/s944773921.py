n = int(input())
if n < 10:
  print(n)
elif 10 <= n < 100:
  print(9)
elif 100 <= n < 1000:
  print(n-90)
elif 1000 <= n < 10000:
  print(909)
elif n == 100000:
  print(90909)
else:
  print(n-9090)