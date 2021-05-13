# coding: utf-8
import math
from collections import deque
import copy
import bisect
k, n = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
m=max(A)
s=k-m
print(max(m-1-s, 0))