# coding:utf-8
import math
while True:
    n = input()
    if n == 0:
        break
    t = [0.0 for i in range(n)]
    a2 = 0.0
    array = map(float,raw_input().split())
    average = sum(array) / n
    for i in range(n):
        t[i] = math.pow(array[i]-average,2)
    a2 = sum(t) / n
    a = math.sqrt(a2)
    print a

