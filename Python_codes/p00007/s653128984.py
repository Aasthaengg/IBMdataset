import math
debt = 100000
rate = 1.05
week = int(input())
for i in range(week):
    debt = math.ceil(debt*1.05/1000)*1000
print(debt)
