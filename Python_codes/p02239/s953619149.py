import math
import copy
import sys
import fractions
# import numpy as np
# import statistics
import decimal
import heapq
import collections
import itertools
import bisect

# from operator import mul

sys.setrecursionlimit(100001)


# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# ===FUNCTION===

def getInputIntList():
    outputDataList = []
    inputData = input().split()
    outputDataList = [int(n) for n in inputData]

    return outputDataList


def getSomeInputInt(n):
    outputDataList = []
    for i in range(n):
        inputData = int(input())
        outputDataList.append(inputData)

    return outputDataList


def getSomeInputListInt(n):
    inputDataList = []
    outputDataList = []
    for i in range(n):
        inputData = input().split()
        inputDataList = [int(n) for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList


# ===CODE===

n = int(input())
adj = [list(map(int, input().split()))[2:] for _ in range(n)]

d = [-1] * n

for a in adj:
    for i in range(len(a)):
        a[i] -= 1

s = 0
q = collections.deque([])
d[s] = 0
q.append(s)
while len(q):
    u = q.popleft()
    v = adj[u]
    for vi in v:
        if d[vi] == -1:
            d[vi] = d[u] + 1
            q.append(vi)
        elif d[vi] > d[u] + 1:
            d[vi] = d[u] + 1
            q.append(vi)

for i, di in enumerate(d):
    print(i + 1, di)

