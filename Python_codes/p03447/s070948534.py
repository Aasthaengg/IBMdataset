import math
money = int(input())
cake= int(input())
donuts = int(input())
money -= cake
num = math.floor(money / donuts)
money -= donuts * num
print(money)