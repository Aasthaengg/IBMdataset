# coding: utf-8
n, x = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)
if A[0] > x:
    A[0] = x
for i in range(n-1):
    s = A[i+1] + A[i]
    if s > x:
        A[i+1] -= s - x
print(S - sum(A))