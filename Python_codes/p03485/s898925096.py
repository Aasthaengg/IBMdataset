a, b = map(int, input().split(" "))
N = (a + b) * 5

if N % 10:
  print(int(str(N)[:-1]) + 1)
else:
  print(int(N / 10))