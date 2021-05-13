A, B, C, K = map(int, input().split())

if(A >= K):
  print(K * 1)
else:
  if(A + B >= K):
    print(A * 1 + B * 0)
  else:
    print(A - (K - A - B))