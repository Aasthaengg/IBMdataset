N,M=list(map(int, input().split()))
K=M-2*N
if K>=0:
  print(N+K//4)
else:
  print(min(N, M//2))
