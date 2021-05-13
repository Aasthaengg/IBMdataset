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
    T = 'CODEFESTIVAL2016'

    print(sum(1 for i in range(16) if S[i] != T[i]))

if __name__ == '__main__':
    main()