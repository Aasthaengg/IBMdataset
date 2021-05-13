#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(1)
    exit()
i = 0
B = []
b = [A[0]]
zouka = 0
f = True
while i < N-1:
    if A[i] == A[i+1]:
        b.append(A[i])
        i += 1
        continue

    if zouka == 0:
        if A[i] < A[i+1]:
            zouka = 1
        else:
            zouka = -1

    if A[i] < A[i+1]: #増加
        if zouka == 1:
            b.append(A[i+1])
        else:
            B.append(b)
            b = [A[i+1]]
            zouka = 0
            
    else: #減少
        if zouka == 1:
            B.append(b)
            b = [A[i+1]]
            zouka = 0
        else:
            b.append(A[i+1])
    i += 1
B.append(b)
print(len(B))
