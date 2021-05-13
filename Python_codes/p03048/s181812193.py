import sys
import copy
import math
import itertools
import numpy as np
import re

R,G,B,N = [int(c) for c in input().split()]
cnt = 0
for r in range(N//R+1):
    for g in range((N-r*R)//G+1):
        if r*R+g*G <= N and (N-r*R-g*G)%B == 0:
            cnt += 1
print(cnt)