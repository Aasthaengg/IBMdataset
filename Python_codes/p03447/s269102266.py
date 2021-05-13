money = int(input())
cake = int(input())
donut = int(input())

x = 1
y = (money - cake)//donut

print(money - cake * 1 - donut * y)