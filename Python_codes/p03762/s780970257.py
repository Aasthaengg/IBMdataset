n, m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
total = 0
x_total = 0
y_total = 0
for i in range(len(x)):
    x_total += x[i] * i - x[i] * (n - (i + 1))
for i in range(len(y)):
    y_total += y[i] * i - y[i] * (m - (i + 1))
print((x_total * y_total) % mod)
