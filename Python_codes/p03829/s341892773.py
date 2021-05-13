n, a, b = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    d = X[i + 1] - X[i]
    ans += min(a * d, b)

print(ans)
