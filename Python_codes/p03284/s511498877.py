n, k = map(int, input().split())
print(n % k if (n % k) == 1 or (n % k) == 0 else 1)
