N, M, K = map(int, input().split())
for i in range(N):
  for j in range(M):
    s = i * j + (N-i) * (M-j)
    if s == K or N*M - s == K:
      print("Yes")
      exit()
print("No")