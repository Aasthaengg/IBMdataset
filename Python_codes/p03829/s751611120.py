n, a, b = map(int, input().split())
X = list(map(int, input().split()))
ans = 0
m = b // a
for i in range(n-1):
  d = X[i+1] - X[i]
  if d > m:
    ans += b
  else:
    ans += a*d
print(ans)