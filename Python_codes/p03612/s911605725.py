#!/usr/bin/env python3

N = int(input())
P = list(map(int, input().split()))

cnt = 0
for i in range(N-1):
    if i+1 == P[i]:
        p = P[i]
        P[i] = P[i+1]
        P[i+1] = p
        cnt += 1

if P[N-1] == N:
    cnt += 1

print(cnt)

