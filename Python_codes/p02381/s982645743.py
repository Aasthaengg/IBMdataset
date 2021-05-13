# coding: utf-8
import math

while True:
    n = int(input())
    
    if n == 0:
        break

    m = 0 # ?????????
    m2 = 0 # 2???????????????
    
    s = map(int,input().split())

    for i in s:
        m += i
        m2 += i ** 2

    m /= n
    m2 /= n

    sd = math.sqrt(m2 - m**2)

    print("{:.8f}".format(sd))