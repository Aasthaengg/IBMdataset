x = int(input())
a = int(input())
b = int(input())
money = x - a
while money >= b:
    money -= b
print(money)