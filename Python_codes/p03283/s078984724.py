import numpy as np
import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
city = np.zeros((N + 2, N + 1), dtype=np.int)

for _ in range(M):
    L, R = map(int, input().split())
    city[L][R] += 1

np.cumsum(city, axis=0, out=city)
np.cumsum(city, axis=1, out=city)

for _ in range(Q):
    p, q = map(int, input().split())
    print(city[q][q] - city[q][p - 1] - city[p - 1][q] + city[p - 1][p - 1])