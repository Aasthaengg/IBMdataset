N,K = map(int,input().split())
if K >= 2:
  if N-K+1 >= 1:
    print(N-K)
  else:
    print(0)
else:
  print(0)