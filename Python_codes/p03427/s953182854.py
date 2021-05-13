import sys, math
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10**9)
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

N = ii()
m = 0
k = N
while k > 0:
    m += k%10
    k //= 10
print(max(m, int(str(N)[0])-1+9*(len(str(N))-1)))