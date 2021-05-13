n, k, x, y = [int(input()) for i in range(4)]

if n - k > 0:
    print(k * x + (n - k) * y)
else:
    print(n * x)

