#!/usr/bin/env python3
# sys.stdin.readline()
import numpy as np
import math
import sys
from collections import defaultdict
input = sys.stdin.readline
s= int(input())

ans = 0
for i in range(100000000):
    ans +=i
    if ans >= s:
        print(i)
        sys.exit() 


