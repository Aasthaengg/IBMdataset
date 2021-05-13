X, K, D = map(int, input().split())
y = abs(X)//D
if y >= K:
  ans = abs(X) - K * D
elif (K - y)%2 == 1:
  ans = abs(abs(X) - y * D - D)
else:
  ans = abs(abs(X) - y * D)
print(ans)