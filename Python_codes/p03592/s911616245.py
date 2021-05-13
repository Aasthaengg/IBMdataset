N, M ,K = map(int, input().split())
# aN + bM - ab =　K となるA,Bが存在するか。

for a in range(M + 1):
  for b in range(N + 1):
    if a * N + b * M - 2 * a * b == K:
      print("Yes")
      exit()
print("No")

