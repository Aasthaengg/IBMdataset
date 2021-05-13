n, a, b = map(int, input().split())

print(max(0,(a + (b * (n - 1))) - (b + (a * (n - 1))) + 1))
