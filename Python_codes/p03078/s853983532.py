import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *
from fractions import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

def main():
    X, Y, Z, K = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()), reverse=True)
    C = sorted(map(int, input().split()), reverse=True)
    h = []
    for i in A:
        for j in B:
            if len(h) < K:
                heappush(h, i + j)
            elif h[0] < i + j:
                heappush(h, i + j)
                heappop(h)
    AB = h[:]
    AB.sort(reverse=True)
    h = []
    for i in AB:
        for j in C:
            if len(h) < K:
                heappush(h, i + j)
            elif h[0] < i + j:
                heappush(h,i + j)
                heappop(h)
    ABC = h[:]
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

main()
