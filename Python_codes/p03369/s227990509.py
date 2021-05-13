topping = str(input())

price = 700

if topping[0]=="o":
  price += 100
if topping[1]=="o":
  price += 100
if topping[2]=="o":
  price += 100

print(price)