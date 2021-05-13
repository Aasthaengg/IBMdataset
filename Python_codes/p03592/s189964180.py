N, M, K = map(int, input().split())
for ic in range(N+1):
  for ir in range(M+1):
    if(N*ir+M*ic-2*ic*ir == K):
      print("Yes")
      exit()
print("No")