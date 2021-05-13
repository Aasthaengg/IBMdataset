# -*- coding: utf-8 -*-
#D - Good Grid
import sys 
from itertools import permutations
from collections import defaultdict
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,C = map(int,readline().split())
D = []
for _ in range(C):
    row = list(map(int,readline().split()))
    D.append(row)
data = []
for _ in range(N):
    row = list(map(int,readline().split()))
    data.append(row)

INF = 10**31
ans = INF
X = defaultdict(int)
Y = defaultdict(int)
Z = defaultdict(int)

for i in range(N):
    for j in range(N):
        pre_c = data[i][j]-1
        if (i+j) % 3 == 0:
            X[pre_c] += 1   
        elif (i+j) % 3 == 1:
            Y[pre_c] += 1
        else:
            Z[pre_c] += 1

M = [i for i in range(C)]
for a,b,c in permutations(M,3):
    total = 0
    for k,v in X.items():
        total += D[k][a]*v
    for k,v in Y.items():
        total += D[k][b]*v
    for k,v in Z.items():
        total += D[k][c]*v
    
    ans = min(ans,total)
print(ans)