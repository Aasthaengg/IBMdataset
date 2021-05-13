from bisect import bisect_left, bisect_right

N, *X = map(int, open(0).read().split())

X.sort()
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k1 = bisect_right(X, X[j] - X[i])
        k2 = bisect_left(X, X[i] + X[j])
        k1 = max(k1, j + 1)
        ans += max(0, k2 - k1)

print(ans)
