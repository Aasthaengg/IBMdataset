A, B, N = map(int,input().split())

if B == 1:
  print(0)
else:
  N = min(N, B-1)
  print(A*N // B)
