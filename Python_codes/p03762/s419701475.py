N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

mod = 10 ** 9 + 7
vx = sum((2 * (k + 1) - N - 1) * X[k] % mod for k in range(N)) % mod
vy = sum((2 * (k + 1) - M - 1) * Y[k] % mod for k in range(M)) % mod
print(vx * vy % mod)
