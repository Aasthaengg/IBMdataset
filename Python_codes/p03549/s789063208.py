#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,M = map(int, input().split())

ans = (M*1900 + (N-M)*100)*(1<<M)
print(ans)