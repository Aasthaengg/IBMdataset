#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
h1, m1, h2, m2, k = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

import datetime as dt
dt1 = dt.datetime.strptime(f'{h1}:{m1}', '%H:%M')
dt2 = dt.datetime.strptime(f'{h2}:{m2}', '%H:%M')
td = dt2 - dt1
print(td.seconds // 60 - k)
