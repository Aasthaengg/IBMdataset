X, K, D = map(int, input().split())
X = abs(X)

m = min(K, X // D)
X -= D * m
K -= m
if K % 2 == 0:
    print(X)
else:
    print(abs(X - D))
