N,K=map(int,input().split())

if N>=K:
  if N%K==0:
    print(0)
  else:
    print(min(N%K,abs(N%K-K)))
else:
  print(min(N,abs(N-K)))