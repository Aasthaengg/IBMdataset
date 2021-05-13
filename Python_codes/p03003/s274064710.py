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
MOD = int(1e+9) + 7

def main():
    N, M = i2nn()
    S = i2nn()
    T = i2nn()

    rui = [[0] * (M + 1) for _ in range(N + 1)]
    #cnt = [[0] * (M) for _ in range(N)]

    n = 1
    for i, s in enumerate(S):
        for j, t in enumerate(T):
            c = 0
            if s == t:
                c += rui[i][j] + 1
            #cnt[i][j] = c
            rui[i+1][j+1] = (rui[i+1][j] + rui[i][j+1] - rui[i][j] + c) % MOD
            n = (n + c) % MOD

    #for v in cnt:
    #    n = (n + sum(v)) % MOD

    #print(rui)
    #print(cnt)
    print(n)

main()
