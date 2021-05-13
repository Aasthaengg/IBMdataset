#!/usr/bin/env python3

N, M = map(int, input().split())

C = {}
for i in range(N):
    C[i+1] = 0

D = {}

for i in range(M):
    P, Y = map(int, input().split())
    D[Y] = [P, i]

ret = {}
for y, p in sorted(D.items(), key=lambda x: x[0]):
    C[p[0]] += 1
    ret[p[1]] = str(p[0]).zfill(6) + str(C[p[0]]).zfill(6)
    
for i, r in sorted(ret.items(), key=lambda x: x[0]):
    print(r)

