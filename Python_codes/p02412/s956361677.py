while True:
  n, x = map(int, [_ for _ in input().split()])
  cnt = 0
  if n == x == 0:
    break

  for n1 in range(1, n+1):
    for n2 in range(n1+1, n+1):
      for n3 in range(n2+1, n+1):
        if n1 != n2 and n2 != n3 and n3 != n1:
          if n1+n2+n3 == x:
            cnt += 1

  print(cnt)