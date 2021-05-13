N, M = map(int, input().split())
if N == 1 and M == 1:
  print(1)
  exit()
if N>=2 and M>=2:
  print((N-2)*(M-2))
else:
  if N == 1:
    print(M-2)
  else:
    print(N-2)

