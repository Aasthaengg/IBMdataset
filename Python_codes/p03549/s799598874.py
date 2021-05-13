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


NM = str(input()).split()
N = int(NM[0])
M = int(NM[1])

p = (1/2)**M
q = 1/p

ans = q*(M*1900)+q*((N-M)*100)

print(int(ans))

