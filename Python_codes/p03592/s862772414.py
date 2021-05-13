N, M, K = map(int, input().split())
f = 0
for i in range(0, N+1):
  if N == 2 * i:
    if K == i * M:
      print("Yes")
      f = 1
      break
  elif (K - i * M) % (N - 2 * i) == 0 and 0 <= (K - i * M) // (N - 2 * i) <= M:
    print("Yes")
    f = 1
    break
if f == 0:
  print("No")