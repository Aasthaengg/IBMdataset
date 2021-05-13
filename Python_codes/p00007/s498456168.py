import math
price = 100000.0
n = int(raw_input())
for i in range(n):
    price = math.ceil((price * 1.05) / 1000) * 1000
print int(price)
