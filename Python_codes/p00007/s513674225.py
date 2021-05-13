# -*- coding: utf-8 -*-

import math

PRINCIPAL = 100000
RATE = 0.05
ABOVE = 1000

n = int(raw_input())
debt = PRINCIPAL
for i in range(n):
    debt = int(math.ceil(float(debt)*(1+RATE)/ABOVE))*ABOVE
print debt