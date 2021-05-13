import itertools
import functools
import math
from collections import Counter
from itertools import combinations
import re

A,B,C = map(int,input().split())

if A==B and B==C:
    print('No')

elif A != B and B != C and C != A:
    print('No')
else:
    print('Yes')
