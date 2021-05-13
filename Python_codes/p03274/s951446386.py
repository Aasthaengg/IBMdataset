N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = float("INF")
for i in range(N-K+1):
  l = i
  r = i + K - 1
  if X[l] * X[r] < 0:
    ans = min(ans, 2 * min(abs(X[l]), abs(X[r])) + max(abs(X[l]), abs(X[r])))
  else:
    ans = min(ans, abs(X[r]) if X[r] > 0 else abs(X[l]))
print(ans)