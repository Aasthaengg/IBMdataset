N, K, X, Y = (int(input()) for i in range(4))
P = 0
for i in range(1,N+1):
  if i <= K:
    P = P + X
  else:
    P = P + Y
print(P)