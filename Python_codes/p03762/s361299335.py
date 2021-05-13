n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

MOD = 10 ** 9 + 7

x_sum = 0
temp = 0
for i in range(n - 1):
    temp = temp + n - 1 - (2 * i)
    x_sum += (x[i + 1] - x[i]) * temp
    x_sum %= MOD

y_sum = 0
temp = 0
for i in range(m - 1):
    temp = temp + m - 1 - (2 * i)
    y_sum += (y[i + 1] - y[i]) * temp
    y_sum %= MOD

print( (x_sum * y_sum) % MOD )
