X, K, D = map(int,input().split())
if X < 0: X *= -1
n = X // D
if K <= n: print(X - K * D)
else:
  X -= n * D
  K -= n
  if K % 2 == 0: print(X)
  else: print(-X + D)