# coding:utf-8
import math
debt = 100000

for _ in range(int(input())):
    debt *= 1.05
    debt = math.ceil(debt / 1000) * 1000

print(debt)

