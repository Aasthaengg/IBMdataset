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

def isPrime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    
    return True

def main():
    N = ii()
    ans = []
    
    k = 2
    while len(ans) < N:
        if isPrime(k) and k%5==1:
            ans.append(k)
        k += 1

    print(*ans)

if __name__ == '__main__':
    main()
