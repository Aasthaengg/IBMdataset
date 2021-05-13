N = int(input())
S = []
if N == 0:
  print(0)
else:
  while N != 0:
    S += [N % 2]
    N -= S[-1]
    N //= - 2
  print(*S[-1::-1], sep='')