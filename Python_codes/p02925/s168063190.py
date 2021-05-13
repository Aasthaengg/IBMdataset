import sys
from collections import defaultdict
from itertools import product, permutations, combinations

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

q = list(range(N))
c = defaultdict(int)
t = [0]*N
r = 0

while q:
    r += 1
    nq = []
    for i in q:
        j = A[i][t[i]] - 1
        k = i
        if k < j:
            j, k = k, j
        c[(j, k)] += 1
        if c[(j, k)] == 2:
            t[j] += 1
            t[k] += 1
            if t[j] < N-1:
                nq.append(j)
            if t[k] < N-1:
                nq.append(k) 
    q = nq

for tt in t:
    if tt != N-1:
        print(-1)
        exit()

print(r)