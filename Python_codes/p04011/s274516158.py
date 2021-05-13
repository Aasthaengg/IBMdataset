day = int(input())
posreday= int(input())
price = int(input())
posreprice = int(input())
if day<= posreday:
  print(day * price)
elif day > posreday:
  print(posreday * price + (day - posreday) * posreprice)