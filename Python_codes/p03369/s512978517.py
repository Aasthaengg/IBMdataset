# -*- coding: utf-8 -*-

s = list(str(input())) # StringをChrのリストに分解

price = 700 + (100 * s.count('o'))

print(price)