N, M, K = map(int, input().split())
p = 'No'
for i in range(N+1):
  for j in range(M+1):
    if i * j + (N - i) * (M - j) == K:
      p = 'Yes'
      break
print(p)