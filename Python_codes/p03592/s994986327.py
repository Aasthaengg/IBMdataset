N, M, K = map(int, input().split())

for x in range(M+1):
  for y in range(N+1):
    if x*N + y*M - 2*x*y == K:
      print('Yes')
      exit()
print('No')