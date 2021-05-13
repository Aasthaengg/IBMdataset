n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

a = []
for i in range(n - 1):
    a.append(x[i+1] - x[i])

b = []
for i in range(m - 1):
    b.append(y[i+1] - y[i])

s = 0
for i in range(1, n):
    s += i * (n - i) * a[i-1]
    s = s % (10 ** 9 + 7)

t = 0
for i in range(1, m):
    t += i * (m - i) * b[i-1]
    t = t % (10 ** 9 + 7)

print((s * t) % (10 ** 9 + 7))
