N, K=map(int, input().split())
m=int(N%K)
M=K-m
if 2*m>K:
  print(M)
else: print(m)