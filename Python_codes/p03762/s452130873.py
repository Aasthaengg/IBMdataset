n, m = map(int, input().split())
X = [int(x) for x in input().split()]
Y = [int(y) for y in input().split()]
p = 10 ** 9 + 7
print(sum([(X[i + 1] - X[i]) * (i + 1) * (n - i - 1) % p for i in range(n - 1)]) * sum([(Y[i + 1] - Y[i]) * (i + 1) * (m - i - 1) % p for i in range(m - 1)]) % p)