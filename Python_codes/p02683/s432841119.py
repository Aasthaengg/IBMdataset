# author:  Taichicchi
# created: 14.09.2020 22:23:14

import sys
from itertools import combinations

N, M, X = map(int, input().split())

C = []
A = []

for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)
comb = [0, 1, 2]

save = []

for choice in range(1, N + 1):
    for comb in combinations(list(range(N)), choice):
        ls = [0 for _ in range(M)]
        for i in comb:
            for m in range(M):
                ls[m] += A[i][m]
            if all(list(map(lambda x: x >= X, ls))):
                save.append(sum([C[_] for _ in comb]))
if save:
    print(min(save))
else:
    print(-1)
