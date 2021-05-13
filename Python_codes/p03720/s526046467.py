#!/usr/bin/env python3

N, M = map(int, input().split())
D = {}
for i in range(1, N+1):
    D[i] = []

for i in range(M):
    a, b = map(int, input().split())
    D[a].append(b)
    D[b].append(a)

for i in range(1, N+1):
    print(len(D[i]))
