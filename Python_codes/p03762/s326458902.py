N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))
Y = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7

X_SUM, Y_SUM = 0, 0
for i, x in enumerate(X):
    X_SUM = (X_SUM + x * (i - (N - i - 1))) % mod

for i, y in enumerate(Y):
    Y_SUM = (Y_SUM + y * (i - (M - i - 1))) % mod

print((X_SUM * Y_SUM) % mod)
