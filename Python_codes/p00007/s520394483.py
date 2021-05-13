#!/usr/bin/python

num = int(raw_input())
money = 100000

for i in range(num):
    money = int(money * 1.05)
    if money % 1000 == 0:
        continue
    else:
        money = int(money) / 1000 * 1000 + 1000
print money