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
    A, B = i2(N)
    
    cnt = 0
    for i in range(N-1, -1, -1):
        cnt += math.ceil((A[i]+cnt)/B[i])*B[i]-(A[i]+cnt)

    print(cnt)

if __name__ == '__main__':
    main()
