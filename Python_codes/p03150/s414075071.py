import sys
import copy
import math
import itertools
import numpy as np
import re

S = input()
s = "keyence"
for i in range(len(S)):
    if re.fullmatch(s[:i]+".*"+s[i:],S):
        print("YES")
        sys.exit(0)

print("NO")