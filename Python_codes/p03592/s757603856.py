# B - fLIP
N, M, K = map(int, input().split())

for i in range(N + 1):
  for j in range(M + 1):
    black = M * i + N * j - i * j * 2
    
    if black == K:
      print('Yes')
      exit()

print('No')