import math
X = int(input())
balance = 100
counter = 0

while balance < X:
    counter += 1
    balance = balance * 101 // 100
print(counter)