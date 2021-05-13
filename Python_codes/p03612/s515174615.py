N, *X = map(int, open(0).read().split())

ans = 0
for i in range(N):
    if X[i] == i + 1:
        if i < N - 1:
            X[i], X[i + 1] = X[i + 1], X[i]
        else:
            X[i - 1], X[i] = X[i], X[i - 1]
        ans += 1

print(ans)
