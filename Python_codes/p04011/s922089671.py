n, k, x, y = map(int, [input() for i in range(4)])
count = 1
price = 0
for i in range(n):
    if count <= k:
        price += x
        count += 1
    else:
        price += y
        count += 1
print(price)