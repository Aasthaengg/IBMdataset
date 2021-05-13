#coding: utf-8

N = int(input())
A = []
B = []
SUM = []
for i in range(N):
    a, b = (int(n) for n in input().split())
    A.append(a)
    B.append(b)
    SUM.append((a+b, i))


SUM.sort(reverse=True)

sumA = 0
sumB = 0
for i in range(N):
    idx = SUM[i][1]
    if i % 2 == 0:
        sumA += A[idx]
    else:
        sumB += B[idx]

print(sumA - sumB)

