num = int(input())
border = int(input())
first = int(input())
second = int(input())

if num <= border:
    price = num*first
else:
    price = border*first
    price += (num - border)*second
    
print(price)