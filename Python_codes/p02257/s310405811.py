#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
?´???°

?´???°??? 1 ??¨????????°??????????????§????????????????????¶??°????´???°??¨?¨?????????????
n ????????´??°???????????????????????????????????????????´???°?????°???????????????????????°????????????????????????????????????
"""
import math

def isPrime(x):
    """ ??¨???????????????????¢¨?´???°?????? """

    if x == 2: # ??¶??°??§?´???°??????????????°
        return True

    if x % 2 == 0: # 2??\????????¶??°????´???°??§?????????
        return False

    rx = int(math.sqrt(x)) + 1
    for i in range(3, rx, 2): # ?????????????????°?????????????????????
        if x % i == 0:
            return False
    return True


# ?????????
n = int(input().strip())
a = []
for i in range(n):
    a.append(int(input().strip()))
cnt = 0
for i in a:
    if isPrime(i) == True:
        cnt += 1

print(cnt)