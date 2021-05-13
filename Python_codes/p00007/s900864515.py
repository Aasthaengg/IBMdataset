import math
n = int(input())
money = 10**5
for i in range(n):
    money *= 1.05
    money_c = math.ceil(money * 0.001)
    money = money_c * 1000
print(money)