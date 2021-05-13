import sys
input = sys.stdin.readline
from collections import *

N, M, Q = map(int, input().split())
A = [[0]*N for _ in range(N)]

for _ in range(M):
    L, R = map(int, input().split())
    A[L-1][R-1] += 1

acc = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        acc[i+1][j+1] = acc[i+1][j]+acc[i][j+1]-acc[i][j]+A[i][j]
    
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    print(acc[q+1][q+1]-acc[q+1][p]-acc[p][q+1]+acc[p][p])