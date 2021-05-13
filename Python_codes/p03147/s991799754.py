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
    H = i2nn()
    op = 0
    while True:
        b = False
        hmax = 0
        for i in range(N):
            if H[i] > 0:
                if b == False:
                    b = True
                    op += 1
                H[i] -= 1
                if hmax < H[i]:
                    hmax = H[i]
            else:
                b = False
        if hmax == 0:
            break
    print(op)

main()
