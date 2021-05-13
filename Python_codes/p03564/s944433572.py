import unittest
from io import StringIO
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    n = int(input())
    K = int(input())
    i = 1
    cnt = 0
    for _ in range(n):
        if i<K:
            i+=i
        else:
            i+=K
    print(i)

    """while i < K:
        i *= 2
        cnt += 1
    print(i+K*(n-cnt))"""


resolve()