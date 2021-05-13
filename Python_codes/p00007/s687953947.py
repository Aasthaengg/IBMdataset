import math
n=int(input())

money = 100000
par = 1.05

for i in range(n):
    up = (money*1.05)/1000
    money = math.ceil(up)*1000
    #print(up*1000, money)
print(money)