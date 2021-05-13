N, K = map(int, input().split())

if K % 2 != 0:
  print((N//K) ** 3)
else:
  dK = N // K
  dK2 = N // (K // 2) - dK
  print(dK ** 3 + dK2 ** 3)