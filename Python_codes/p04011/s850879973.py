N,K,X,Y = map(int,open(0).read().split())

if N<=K:
  print(int(N*X))
else:
  print(int(K*X+(N-K)*Y))