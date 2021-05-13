X,K,D = map(int,input().split())
X = abs(X)
X_div_D = X//D

ans_min = X % D

if K <= X_div_D:
  print(X - K * D)
else:
  if (K % 2) ^ (X_div_D % 2) == 0:
    print(ans_min)
  else:
    print(abs(ans_min - D))