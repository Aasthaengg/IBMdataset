import math
n = int(input())
money = 100
for i in range(n):
    money = math.ceil(money*1.05)
print(money*1000)