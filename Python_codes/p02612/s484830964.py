N = int(input())
if N % 1000 == 0:
  print(0)
else:
  div = int(N / 1000)
  exc = (div +1)*1000 - N
  print(exc)
