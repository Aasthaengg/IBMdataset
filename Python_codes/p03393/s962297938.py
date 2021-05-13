import sys, math
from functools import lru_cache
from collections import defaultdict
from decimal import Decimal
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

def main():
    S = input()
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        return

    l = [0]*26
    for c in S:
        l[ord(c)-ord('a')] += 1

    if len(S) < 26:
        i = l.index(0)
        print(S+chr(i+ord('a')))
        return

    for i in range(len(S)-1, 0, -1):
        if S[i-1] < S[i]:
            break

    c = min(S[j] for j in range(i, len(S)) if S[j] > S[i-1])
    print(S[:i-1]+c)

if __name__ == '__main__':
    main()
