n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10 ** 9 + 7
X = 0
Y = 0
for i in range(n - 1):
  t = x[i + 1] - x[i]
  X = (X + (i + 1) * (n - i - 1) * t) % MOD
for i in range(m - 1):
  t = y[i + 1] - y[i]
  Y = (Y + (i + 1) * (m - i - 1) * t) % MOD
print(X * Y % MOD)