n, k, x, y = map(int, open(0).read().split())
print(min(n,k)*x + max(0, (n-k))*y)