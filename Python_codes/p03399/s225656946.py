# -*- coding: utf-8 -*-

a = int(input())
b = int(input())
c = int(input())
d = int(input())

train = 0
bus = 0

train = a if a < b else b
bus = c if c < d else d

print(train + bus)