MOD = 10 ** 9 + 7
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_sum = 0
for k, value in enumerate(x):
    x_sum += (2 * (k + 1) - n - 1) * value
    x_sum %= MOD

y_sum = 0
for k, value in enumerate(y):
    y_sum += (2 * (k + 1) - m - 1) * value
    y_sum %= MOD

print ((x_sum * y_sum) % MOD)



