N, A, B = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]
p = [B] * (N - 1)
for i in range(N - 1):
    if (X[i + 1] - X[i]) * A < B:
        p[i] = (X[i + 1] - X[i]) * A
print(sum(p))
