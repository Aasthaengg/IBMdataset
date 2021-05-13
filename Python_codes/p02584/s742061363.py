X,K,D = map(int, input().split())

X = abs(X)
ans = 0
if K*D < X:
  ans = X - K*D
else:
  if (K - X // D) % 2 == 0:
    ans = X % D
  else:
    ans = abs(X % D - D)
print(ans)