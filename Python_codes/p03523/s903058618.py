import sys, math, re
from functools import lru_cache
from collections import defaultdict
sys.setrecursionlimit(500000)
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
    S = input()
    l = [0, 4, 6, 8]
    ok = []

    for i in range(2**4):
        w = ['', 'K', 'I', 'H', '', 'B', '', 'R', '']
        for j in range(4):
            if (i>>j)&1:
                w[l[j]] = 'A'
        ok.append(''.join(w))

    print('YES' if S in ok else 'NO')

if __name__ == '__main__':
    main()