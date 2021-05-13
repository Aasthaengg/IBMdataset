N, T = map(int, input().split())
X = tuple(map(int, input().split()))
p = X[0]
ans = max(X) + T - p
for x in X:
    if x - p > T:
        ans -= (x - p) - T
    p = x

print(ans)
