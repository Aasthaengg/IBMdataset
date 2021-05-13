a, b = map(int, input().split())

if a >= 13:
    price = b
elif a >= 6 and a <= 12:
    price = b/2
else:
    price = 0

print(int(price))