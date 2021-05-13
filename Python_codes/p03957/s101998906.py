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
    s = input()
    n = len(s)

    for i in range(n):
        if s[i] == 'C':
            for j in range(i+1, n):
                if s[j] == 'F':
                    print('Yes')
                    return

    print('No')


if __name__ == '__main__':
    main()