import sys
import copy
import math
import itertools
import numpy as np
import re

N,T = [int(c) for c in input().split()]
t = [int(c) for c in input().split()]

ans = T
for i in range(1,N):
    if t[i]-t[i-1] < T:
        ans += t[i]-t[i-1]
    else:
        ans += T

print(ans)