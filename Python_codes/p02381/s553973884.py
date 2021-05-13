#!/usr/bin/env python
import statistics
import math

allData = []

while True:
    n = int(input())
    if n == 0:
        break
    data = input().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    allData.append(data)

for x in allData:
    print(math.sqrt(statistics.pvariance(x)))