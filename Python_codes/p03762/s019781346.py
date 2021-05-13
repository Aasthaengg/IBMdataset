N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

mod = 10**9 + 7

X = 0
Y = 0
for i in range(N - 1):
    X += (A[i + 1] - A[i]) * (i + 1) * (N - 1 - i)
    X %= mod
for j in range(M - 1):
    Y += (B[j + 1] - B[j]) * (j + 1) * (M - 1 - j)
    Y %= mod
print(X * Y % mod)
