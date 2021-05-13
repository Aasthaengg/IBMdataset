n, a, b = map(int, input().split())

price = [a * n] + [b]
print(min(price))
