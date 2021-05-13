import math
price = int(input())
tax = 8
price_1 = math.ceil(price / (1 + tax / 100))
price_2 = math.floor(price_1 * tax / 100)
print(price_1 if price == price_1 + price_2 else ':(')