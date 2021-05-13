n, k, x, y = [int(input()) for _ in range(4)]
print(x * k + y * (n - k) if n > k else x * n)