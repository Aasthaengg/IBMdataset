import sys
sys.setrecursionlimit(100000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from math import *
from copy import *

n = int(input())
a = list(map(int, input().split()))+[-1]
k = []
t = 1
for i in range(n):
    if a[i] == a[i+1]:
        t += 1
    else:
        if t > 1:
            k.append(t)
            t = 1
ans = 0
for x in k:
    ans += x//2
print(ans)
