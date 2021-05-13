import sys
import copy
import math
import itertools
import numpy as np

A,B,C = [int(c) for c in input().split()]
a = []
cnt=0
while True:
    cnt+=A
    a.append(cnt%B)
    if C == cnt%B:
        print("YES")
        sys.exit(0)
    elif a.count(cnt%B) >1:
        print("NO")
        sys.exit(0)