n, a, b, *x = map(int, open(0).read().split())
print(sum(min((j - i) * a, b) for i, j in zip(x, x[1:])))