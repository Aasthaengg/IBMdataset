import math
money = int(100)
for i in range(int(input())):
    money *= 1.05
    money = math.ceil(money)
print(int(money) * 1000)
