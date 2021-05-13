# coding: utf-8
from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cnt = 1
for i in range(1, N):
    if A[0] == A[i]:
        cnt += 1
print(ceil((N-cnt)/(K-1)))