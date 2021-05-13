import sys
from collections import deque  # 双方向キュー
from collections import defaultdict  # 初期化済み辞書
from heapq import heapify, heappush, heappop, heappushpop  # プライオリティキュー
from bisect import bisect_left, bisect_right  # 二分探索
#import numpy as np  # 1.8.2
#import scipy  # 0.13.3

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

def main():
    N = i2n()
    A = i2nn()
    A.sort()
    a0 = A[0]
    a3 = A[N-1]
    A12 = A[1:N-1]
    iz = bisect_left(A12, 0)
    A1 = A12[:iz]
    A2 = A12[iz:]

    logs = []
    def logging(x, y):
        logs.append('%d %d' % (x, y))
        return x - y
    x = a0
    for y in A2:
        x = logging(x, y)
    y = x
    x = a3
    x = logging(x, y)
    for y in A1:
        x = logging(x, y)
    print(x)
    for log in logs:
        print(log)

main()
