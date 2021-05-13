N = int(input())

for h in range(1, 3501):
  for n in range(h, 3501):
    if (4 * h * n - N * n - h * N) == 0:
      continue
    w = (N * h * n) / (4 * h * n - N * n - h * N)
    if w.is_integer() and 1 <= w < 3501:
      print(h, n, int(w))
      exit()