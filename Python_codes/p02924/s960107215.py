# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())

from decimal import Decimal
ret = Decimal(n/2)*Decimal(n-1)
print(int(ret))