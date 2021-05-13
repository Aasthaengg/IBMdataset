## coding: UTF-8
from decimal import *
from itertools import permutations, combinations,combinations_with_replacement,product
import math

s = input()
l = []
#for i in range(len(s)):
    #l.append(s[i])
for i in range(0, len(s), 2):
    l.append(s[i])

print('{}'.format(''.join(l)))