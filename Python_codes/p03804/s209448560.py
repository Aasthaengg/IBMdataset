# -*- coding: utf-8 -*-

N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    A.append(list(map(str, input())))

for i in range(M):
    B.append(list(map(str, input())))

tmp = []
for i in range(N - M + 1):
    for j in range(N - M + 1):
        tmp = []
        for k in range(M):
            tmp.append(A[i + k][j:j+M])
        # 判定
        if tmp == B:
            print('Yes')
            exit()

print('No')