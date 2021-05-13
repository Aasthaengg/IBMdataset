n = int(input())
blue = [input() for _ in range(n)]

m = int(input())
red = [input() for _ in range(m)]

price_max = 0
for a in blue:
    if (blue.count(a) - red.count(a)) > price_max:
        price_max = blue.count(a) - red.count(a)
print(price_max)