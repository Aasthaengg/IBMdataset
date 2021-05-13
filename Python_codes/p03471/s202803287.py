N, Y = map(int, input().split())
a = min(Y // 10000, N) + 1
for i in range(a):
  b = min((Y - (10000 * i)) // 5000, N - i) + 1
  for j in range(b):
    if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y:
      print(i, j, N - i - j)
      break
  else:
    continue
  break
else:
  print('-1 -1 -1')