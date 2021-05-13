import math
up_rate = 1.01
money = 100

TARGET = int(input())

counter = 0
while TARGET > money:
    money += money // 100
    counter += 1
    # print(counter, money)
    
print(counter)