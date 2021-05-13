x = int(input())

price = 100
count = 0

while price < x :
  price += price//100
  count += 1

print(count)