age, price = map(int, input().split())

if 13 <= age <= 100:
  price = price
  
elif 6 <= age <= 12:
  price = price // 2
  
elif 0 <= age <= 5:
  price = 0
  
print(price)