import math
n = int(input())

price = n / 1.08
if math.floor(math.floor(price) * 1.08) == n:
    print(math.floor(price))
elif math.floor(math.ceil(price) * 1.08) == n:
    print(math.ceil(price))
else:
    print(':(')