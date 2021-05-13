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
    S = input()
    a, b, c = 0, 0, 0
    for char in S:
        if char == 'a':
            a += 1
        if char == 'b':
            b += 1
        if char == 'c':
            c += 1

    if max(a, b, c)-min(a, b, c) <= 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
