import math
n = int(input())
debt = 100000
for i in range(n):
    debt *= 1.05
    debt = math.ceil(debt/1000)*1000
print(debt)