N = int(input())

h, n, w = 0, 0, 0

for i in range(1, 3501):
  for j in range(i, 3501):
    if (4 * i * j - N * (i + j)) > 0 and (N * i * j) % (4 * i * j - N * (i + j)) == 0:
      h = i
      n = j
      w = (N * h * n) // (4 * h * n - N * (h + n))
      break
  if w != 0:
    break

print(h, n, w)