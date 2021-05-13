#coding: utf-8
import math

while True:
    n = int(input())
    if n == 0:
        break
    s = [float(i) for i in input().split(" ")]
    m = 0

    for i in s:
        m += i
    m /= n

    a2 = 0
    for i in s:
        a2 += (i-m)**2/n

    print(math.sqrt(a2))

