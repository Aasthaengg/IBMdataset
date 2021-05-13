def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)

N = getN()
nums = [int(e) for e in input().split()]
nums.sort()
checker = nums[0]
count = 1
for i in range(1,N):
    if(checker != nums[i]):
        count+=1
        checker = nums[i]
if(N - count)%2==0:
    print(count)
else:
    print(count-1)