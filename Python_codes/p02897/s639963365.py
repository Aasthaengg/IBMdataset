n = int(input())
print((((n + 1) // 2) / n, 0.5)[n % 2 == 0])