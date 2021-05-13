n, a, b = map(int, input().split())

mini = a * (n - 1) + b
maxi = b * (n - 1) + a

print(max(maxi - mini + 1, 0))