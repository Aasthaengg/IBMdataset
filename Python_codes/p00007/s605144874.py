import math
weeks = int(input())
money = 100000
for i in range(weeks):
    money = money * 1.05
    money = money / 1000
    money = math.ceil(money)
    money = money * 1000
print(money)