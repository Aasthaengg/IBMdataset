a, b, c = list(map(int, input().split()))

price = []
price.append(a + b)
price.append(a + c)
price.append(b + c)
print(min(price))
