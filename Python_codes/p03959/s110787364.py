# -*- coding: utf-8 -*-
N = int(input())
T = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))


prev = -1
candidates_t = [-1 for _ in range(N)]
for i in range(N):
    if T[i] != prev:
        candidates_t[i] = T[i]

    prev = T[i]


prev = -1
candidates_a = [-1 for _ in range(N)]
for i in range(N-1, -1, -1):
    if A[i] != prev:
        candidates_a[i] = A[i]

    prev = A[i]

ret = 1
for i in range(N):
    if candidates_t[i] == -1 and candidates_a[i] == -1:
        ret *= min(T[i], A[i])
        ret %= 10**9 + 7

    elif candidates_t[i] == -1:
        if T[i] < candidates_a[i]:
            ret *= 0

    elif candidates_a[i] == -1:
        if A[i] < candidates_t[i]:
            ret *= 0

    elif candidates_t[i] != candidates_a[i]:
        ret *= 0


print(ret)


