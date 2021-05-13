# solution

import io
import sys
import math
from itertools import accumulate as acc
import numpy as np
from collections import Counter

data = int(input())
array = list(map(int, input().split(" ")))

MIN = min(array)
MAX = max(array)

print(2 * data - 1)

if abs(MAX) > abs(MIN):
    index = np.argsort(array)[-1] + 1
    for i in range(1, data + 1):
        if i != index:
            print(index, i)
    print(index, index)
    for i in range(1, data):
        print(i, i + 1)
else:
    index = np.argsort(array)[0] + 1
    for i in range(1, data + 1):
        if i != index:
            print(index, i)
    print(index, index)
    for i in range(1, data)[::-1]:
        print(i + 1, i)