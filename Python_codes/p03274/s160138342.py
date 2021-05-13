n,k = map(int,input().split())
X = list(map(int, input().split()))

ans = 10**10
for i in range(n-k+1):
  d1 = abs(X[i]) + abs(X[i] - X[i+k-1])
  d2 = abs(X[i+k-1]) + abs(X[i] - X[i+k-1])
  if ans > min(d1, d2):
    ans = min(d1,d2)
if ans == 10**10:
  print(0)
else:
  print(ans)


