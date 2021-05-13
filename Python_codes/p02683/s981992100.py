#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    inf = 10**18

    # bit全探索
    # repeat=2だと(0,0), (0,1), (1,0), (1,1)になる
    ans = inf
    for i in product([0,1], repeat=N):
        ok = True
        for m in range(1, M + 1):
            s = 0
            for n in range(N):
                if i[n] == 1:
                    s += A[n][m]
            if s < X:
                ok = False
                break
        if ok:
            money = 0
            for n in range(N):
                if i[n] == 1:
                    money += A[n][0]
            ans = min(ans, money)

    if ans == inf:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
