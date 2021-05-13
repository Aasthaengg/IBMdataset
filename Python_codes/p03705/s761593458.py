n, a, b = [int(x) for x in input().split()]
val = max(0, (a + (n - 1) * b) - ((n - 1) * a + b) + 1)
print(val)