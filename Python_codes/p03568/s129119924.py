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
    A = list(mi())
    cnt = 0
    
    p = [1]*N
    for j in range(N-1):
        p[j+1] = 3*p[j]

    for i in range(3**N):
        B = [0]*N
        flg = False
        for j in range(N):
            t = (i//p[j])%3
            if t == 0:
                B[j] = A[j]
            if t == 1:
                B[j] = A[j]+1
            if t == 2:
                B[j] = A[j]-1

            if B[j]%2 == 0:
                flg = True
        
        if flg:
            cnt += 1

    print(cnt)

        

if __name__ == '__main__':
    main()
