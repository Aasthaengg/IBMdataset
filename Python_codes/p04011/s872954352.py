list = []
price = 0

for i in range(4):
    list.append(int(input()))

for i in range(list[0]):
    if i < list[1]:
        price += list[2]
    else:
        price += list[3]

print(price)