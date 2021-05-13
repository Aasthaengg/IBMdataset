import sys
from itertools import combinations
import math


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


A, B, K = LI()
temp = 0
for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        temp += 1
        if temp == K:
            print(i)
            exit()
