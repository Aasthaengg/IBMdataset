s = str(input())
price = 700
for i in range(3):
    if s[i] == 'o':
        price += 100
print(price)