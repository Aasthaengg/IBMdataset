import sys
from itertools import combinations
import math


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


N = I()
ans = 0
for i in range(1, N+1):
    temp = str(i)
    if len(temp) % 2 == 1:
        ans += 1
print(ans)
