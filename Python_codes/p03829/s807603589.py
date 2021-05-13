n, a, b = map(int, input().split())
X = tuple(map(int, input().split()))
ans = 0
for x0, x1 in zip(X[:n-1], X[1:]):
    ans += min(b, a*(x1-x0))
print(ans)