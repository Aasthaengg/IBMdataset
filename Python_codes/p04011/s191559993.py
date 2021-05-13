N,K,X,Y = map(int,open(0))
a = N*X

if K<N:
  print(a-(X-Y)*(N-K))
else:
  print(a)