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

def f(t, c):
    res = ''
    for i in range(len(t)-1):
        if t[i] == c or t[i+1] == c:
            res += c
        else:
            res += t[i]
    return res

S = input()
ans = 1000
for c in 'qwertyuiopasdfghjklzxcvbnm':
    T = S[:]
    cnt = 0
    while not all(t == c for t in T):
        T = f(T, c)
        cnt += 1
    ans = min(ans, cnt)

print(ans)
