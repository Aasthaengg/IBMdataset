import math

x = int(input())
bank = 100

y = 0
while bank < x:
    bank += int(str(bank)[:-2])
    y += 1
print(y)
