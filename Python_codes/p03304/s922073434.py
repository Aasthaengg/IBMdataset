N, M, D = map(int, input().split())

if N - 2 * D > 0:
  if D == 0:
    print(((N - 2 * D) + 2 * D) / N ** 2 * (M - 1))
  else:
    print(((N - 2 * D) * 2 + 2 * D) / N ** 2 * (M - 1))
else:
  print((M - 1) / N)