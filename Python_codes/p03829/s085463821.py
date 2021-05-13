
N, A, B, *X = map(int, open(0).read().split())

ans = 0
for i in range(N - 1):
    x = A * (X[i + 1] - X[i])
    if x < B:
        ans += x
    else:
        ans += B

print(ans)
