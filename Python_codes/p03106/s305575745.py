import sys
from collections import deque
from itertools import *


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


A, B, K = LI()
l = []
for i in range(1,100+1):
    if A % i == 0 and B % i == 0:
        l.append(i)

l.reverse()
print(l[K-1])
