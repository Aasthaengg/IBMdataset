N, M = map(int, input().split())
X = sorted(list(map(int, input().split())), reverse=True)
Y = sorted(list(map(int, input().split())), reverse=True)
MOD = 10 ** 9 + 7

X_sum = 0
for i, x in enumerate(X, start=1):
    X_sum += x * (N - i - i + 1)
    X_sum %= MOD

Y_sum = 0
for i, y in enumerate(Y, start=1):
    Y_sum += y * (M - i - i + 1)
    Y_sum %= MOD

print(X_sum * Y_sum % MOD)
