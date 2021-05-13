import sys, math
from functools import lru_cache
from collections import deque

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
    b = list(mi())
    K = sum(b) - sum(a)

    if sum(max(0, (b[i]-a[i]+1)//2) for i in range(N)) <= K:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
