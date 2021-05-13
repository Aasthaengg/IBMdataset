import numpy as np
import math

n = int(input())
a = list(map(int, input().split(" ")))

min = 2
max = 2

for i in reversed(a):
    min = math.ceil(min / i) * i
    max = math.floor(max / i) * i + i - 1
    if(min > max):
        print(-1)
        exit()

print("%d %d" %(min, max))