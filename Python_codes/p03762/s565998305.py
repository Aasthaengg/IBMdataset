n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

X = sum([(2*(k+1) - n - 1) * x[k] for k in range(n)])
Y = sum([(2*(k+1) - m - 1) * y[k] for k in range(m)])

print(X * Y % (10**9+7))
