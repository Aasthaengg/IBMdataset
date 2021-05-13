import sys
from itertools import combinations
import math


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


A = I()
B = I()
C = I()
X = I()
ans = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if a*500+b*100+c*50 == X:
                ans += 1
print(ans)
