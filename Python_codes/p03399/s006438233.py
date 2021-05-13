price = []
a = int(input())
b = int(input())
c = int(input())
d = int(input())

price.append(a + c)
price.append(a + d)
price.append(b + c)
price.append(b + d)

print(min(price))
