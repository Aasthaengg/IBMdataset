#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

Q = int(input())

L = []
R = []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)


def primes(max_r):
    is_prime = [True] * (max_r + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(max_r**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, max_r + 1, i):
            is_prime[j] = False
    return [i for i in range(max_r + 1) if is_prime[i] and is_prime[(i+1)//2]]


max_r = max(R)
ps = primes(max_r)

S = [0]
for i in range(1, max_r+1):
    if i in ps:
        S.append(S[i-1]+1)
    else:
        S.append(S[i-1])


for i in range(Q):
    print(S[R[i]] - S[L[i]-1])


