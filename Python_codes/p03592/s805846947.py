N,M,K = map(int,input().split())

for x in range(N+1):
  for y in range(M+1):
    kuro = x*(M-y)+y*(N-x)
    if kuro == K:
      print("Yes")
      exit()
print("No")