# coding: utf-8
# Here your code !
N, M = map(int, input().split())

A = []
b = []

for _ in range(N):
    A.append([int(i) for i in input().split()])
    
for _ in range(M):
    b.append(int(input()))
    
for i in range(N):
    print(sum([A[i][j] * b[j] for j in range(M)]))