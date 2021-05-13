from decimal import *

import numpy as np

import math

if __name__ == '__main__':
    n = int(input())
    count = 0

    for i in range(n):
        b, c = map(str, input().split())
        if c =="JPY":
            count+=int(b)
        else:
            count+=  Decimal(380000 ) * Decimal(b)

    print(count)

