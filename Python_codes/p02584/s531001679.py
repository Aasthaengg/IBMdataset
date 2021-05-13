X, K, D = map(int, input().split())
X = abs(X)
if K <= X//D:
  print(X-D*K)
elif (K-X//D)%2 == 0:
  print(X%D)
else:
  print(D-X%D)