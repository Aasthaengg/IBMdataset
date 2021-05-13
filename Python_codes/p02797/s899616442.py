N, K, S = map(int, input().split())

for i in range(N):
  if 0 < K:
    print(S)
    K-=1
  else:
    if S-1 < 100:
      print(S+1)
    else:
      print(S-1)