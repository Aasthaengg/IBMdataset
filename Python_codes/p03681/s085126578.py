N, M = map(int, input().split())
mod = 10 ** 9 + 7
if abs(N - M) >= 2:
  print(0)
else:
  if abs(N - M) == 1:
    ans = 1
    for i in range(1, N+1):
      ans = ans * i % mod
    for i in range(1, M+1):
      ans = ans * i % mod
    print(ans)
  else:
    ans = 2
    for i in range(1, N+1):
      ans = ans * i % mod
    for i in range(1, M+1):
      ans = ans * i % mod
    print(ans)