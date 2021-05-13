import sys, math
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10**9)

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

    a.sort(reverse=True)

    print(sum(a[1::2][:N]))

    

if __name__ == '__main__':
    main()
