n, m = map(int, input().split())
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]

mod = 10 ** 9 + 7
a = 0
for k in range(n):
    a += k * x[k] - (n - (k + 1)) * x[k]
b = 0
for k in range(m):
    b += k * y[k] - (m - (k + 1)) * y[k]

print(a * b % mod)