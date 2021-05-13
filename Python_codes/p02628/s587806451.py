n, k = (int(x) for x in input().split())
list_p = sorted([int(y) for y in input().split()])
price = 0

for i in range(0, k):
    price += list_p[i]

print(price)