# coding:utf-8

import sys
import math
import time
#import numpy as np
import collections
from collections import deque
import queue
import copy


#X = str(input()).split()
#a = [int(x) for x in input().split()]


N = int(input())
A = [int(x) for x in input().split()]

A2 = list(set(A))

k = len(A) - len(A2)

ans = len(A)-2*math.ceil(k/2)

print(ans)

