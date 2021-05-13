# coding: utf-8
# Your code here!
import math
from decimal import Decimal
a, b, c = map(int, input().split())
if Decimal(str(a * b))**Decimal('0.5') >= Decimal(str((c - a - b) / 2)):
  print('No')
else:
  print('Yes')
