import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def input(): return sys.stdin.readline().rstrip()


N = int(input())
l = deque()
if N == 0:
    print(0)
else:
    while N != 0:
        x = (-2) ** len(l)
        y = (-2) * x
        if abs(N) % abs(y) != 0:
            N -= x
            l.appendleft('1')
        else:
            l.appendleft('0')
    print(''.join(l))