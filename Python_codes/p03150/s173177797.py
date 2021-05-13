#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
s  = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

query = list('keyence')

import re

for p in range(8):
    b = ''.join(query[:p])
    a = ''.join(query[p:])

    pattern1 = r'{}{}'.format(b, a)
    pattern2 = r'^{}.*{}$'.format(b, a)
    #print(re.findall(pattern1, s))
    #print(re.findall(pattern2, s))
    if re.findall(pattern1, s) or re.findall(pattern2, s):
        print('YES')
        break
else:
    print('NO')

