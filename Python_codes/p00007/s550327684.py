import math
money=100.000
for i in range(int(input())):
    money*=1.05
    money=math.ceil(money)
print(money*1000)
