from __future__ import division
import math

while True:
    n = int(raw_input())
    if n == 0:
        break
    data = map(float, raw_input().split())
    m = sum(data) / n
    var = sum([(i-m)**2 for i in data]) / n
    std = math.sqrt(var)
    print "{:.5f}".format(std)