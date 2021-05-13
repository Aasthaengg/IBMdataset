#!/usr/bin/env python

numbers = []
sumN = []
while True:
    number = input()
    if number == '0':
        break
    numbers.append(number)
    
for x in numbers:
    value = 0
    for y in x:
        value += int(y)
    sumN.append(value)

for x in sumN:
    print(x)