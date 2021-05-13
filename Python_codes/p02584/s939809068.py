X, K, D = list(map(int, input().split()))
X = abs(X)

zan = X%D


K2 = K-X//D
if K2 < 0:
  print(X-D*K)
else:
  if K2%2 == 0:
  	print(zan)
  else:
  	print(D-zan)