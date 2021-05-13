N,M=map(int,input().split())
N,M=max(N,M),min(N,M)
if N == 1 and M == 1:
  print(1)
elif N == 2 and M == 1:
  print(0)
elif M == 1:
  print(N-2)
elif M == 2:
  print(0)
else:
  print((N-2)*(M-2))