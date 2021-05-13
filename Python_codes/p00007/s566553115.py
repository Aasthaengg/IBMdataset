# coding: utf-8
# Here your code !
import math

DEBT = 100000.0
n=int(input())
for i in range(n):
    DEBT = int(math.ceil( (DEBT*1.05)/1000.0 )) * 1000
print(DEBT)