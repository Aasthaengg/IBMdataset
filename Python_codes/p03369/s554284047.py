s = list(input())
price = int(700)

for i in s:
    if i == "o":
        price += 100

print(price)