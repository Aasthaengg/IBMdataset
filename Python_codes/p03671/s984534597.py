# A - ringring
a, b, c = [int(s) for s in input().split()]
total_prices = [a + b, b + c, c + a]
print(min(total_prices))