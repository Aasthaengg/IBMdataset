N, A, B = map(int, input().split())

if (B - A)%2 == 0:
  print((B - A) // 2)

else:
  if A - 1 > N - B:
    tmp = N - B
    B = N
    A = A + tmp + 1
    print((B - A) // 2 + tmp + 1)

  else:
    tmp = A - 1
    A = 1
    B = B - tmp - 1
    print((B - A) // 2 + tmp + 1)