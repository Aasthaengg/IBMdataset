import math

n=input()
money = 100000
for i in range(n):
    money = math.ceil(money * 1.05/1000)*1000
print "%d" %(money)