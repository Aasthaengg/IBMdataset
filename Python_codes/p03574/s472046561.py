
#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(input())
    return x

H,W = map(int,input().split())
S = int_mtx(H)
Scopy = S.copy()
for i in range(0,H):
    Scopy[i] = list(Scopy[i])

for i in range(0,H):
    for j in range(0,W):

        if S[i][j] == ".":
            cnt = 0
            for k in range(max(0,i-1),min(i+2,H)):
                for l in range(max(0,j-1),min(j+2,W)):
                    if S[k][l] == "#":
                        cnt += 1
            Scopy[i][j] = str(cnt)

for i in range(0,H):
    print("".join(Scopy[i]))