import sys
s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2sss = lambda n: [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))
from collections import deque  # 双方向キュー
from collections import defaultdict  # 初期化済み辞書
from heapq import heapify, heappush, heappop, heappushpop  # プライオリティキュー
from bisect import bisect_left, bisect_right  # 二分探索
sys.setrecursionlimit(int(1e+6))
MOD = int(1e+9) + 7
#import numpy as np  # 1.8.2
#import scipy  # 0.13.3

def main():
    N = i2n()
    A = i2nn()
    A.sort()
    A.reverse()
    # 5 4 3 2 1 1
    # 0: 5
    # 5: 5 4
    # 9: 5 3 4
    # 13: 5 3 4 2
    # 16: 5 1 3 4 2
    # 19: 5 1 3 1 4 2
    n = 0
    for i in range(1, N):
        n += A[i // 2]
    print(n)

main()
