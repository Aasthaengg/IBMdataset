# coding:utf-8

import sys
import math
import time
#import numpy as np
import collections
from collections import deque
from collections import Counter
import queue
import copy
import bisect
import heapq
import itertools

#sys.setrecursionlimit(10**7)
#N, Q = map(int, input().split())
#G = [list(input()) for i in range(H)]
#INF = V * 10001
#A = [int(i) for i in input().split()]
#AB = [list(map(int, input().split())) for _ in range(K)]

N = int(input())
ans = (N-1)*(N)//2
print(int(ans))
