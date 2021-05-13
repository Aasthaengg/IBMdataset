import sys, math
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
    N = ii()
    a = list(mi())
    s = 0
    for i in range(N):
        s ^= a[i]

    if s != 0:
        print('No')
        return

    if N%3 == 0:
        d = {}
        for i in range(N):
            if not a[i] in d:
                d[a[i]] = 0
            d[a[i]] += 1

        if (len(d) == 1 and 0 in d) or (2 <= len(d) <= 3 and all(v%(N//3) == 0 for v in d.values())):
            print('Yes')
        else:
            print('No')

    else:
        if all(a[i] == 0 for i in range(N)):
            print('Yes')
        else:
            print('No')



if __name__ == '__main__':
    main()