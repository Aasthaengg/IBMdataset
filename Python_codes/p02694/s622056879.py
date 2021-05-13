import math
x = int(input())
balance = 100
years = 0
while True:
    balance = balance * 101
    balance = balance // 100
    years += 1
    if balance >= x:
        break
print(years)