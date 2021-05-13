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

S = input()
i = 1
r = len(S)
while True:
    if i >= len(S):
        break
    if S[i] == S[i-1]:
        r -= 1
        i += 2
    i += 1

print(r)