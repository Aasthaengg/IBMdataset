# -*- coding: utf-8 -*-
X, Y = map(int, input().split())
results = list()
num = X
while num <= Y:
    results.append(num)
    num += num
print(len(results))