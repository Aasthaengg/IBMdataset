import sys
import copy
import math
import itertools
import numpy as np
S = input()
for i in "abcdefghijklmnopqrstuvwxyz":
    if S.count(i) == 0:
        print(i)
        sys.exit(0)

print("None")