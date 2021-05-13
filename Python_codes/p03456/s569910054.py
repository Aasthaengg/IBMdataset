# -*- coding: utf-8 -*-
import math

# スペース区切りの整数の入力
a, b = map(int, input().split())

c = b
if (b < 10):
    c += a*10
elif (b < 100):
    c += a * 100
else:
    c += a * 1000

if ( math.sqrt(c) % 1 == 0 ):
    print("Yes")
else:
    print("No")
