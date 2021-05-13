# x, y = [int(input()) for i in range(2)]
n, k, x, y = [int(input()) for i in range(4)]

if n > k:
    print(int(k * x + y * (n - k)))
else:
    print(int(n * x))
