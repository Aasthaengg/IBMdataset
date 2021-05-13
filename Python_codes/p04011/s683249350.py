n, k, x, y = map(int, [input() for i in range(4)])

if k <= n:
    total = k*x + (n-k)*y
else :
    total = n*x

print(total)