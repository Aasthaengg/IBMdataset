import sys, math
from functools import lru_cache
import numpy as np
from collections import defaultdict
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N = ii()
    S = [input() for i in range(N)]

    k = sum(S[i].count('AB') for i in range(N))

    c = sum(1 for i in range(N) if S[i][-1] == 'A' and S[i][0] == 'B')
    a = sum(1 for i in range(N) if S[i][-1] == 'A') - c
    b = sum(1 for i in range(N) if S[i][0] == 'B') - c

    ans = k+c+min(a,b)
    if c > 0 and a == b == 0:
        ans -= 1
    print(ans)


if __name__ == '__main__':
    main()
