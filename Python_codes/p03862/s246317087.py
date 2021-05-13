# coding: utf-8
n, x = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)
for i in range(n-1):
    s = A[i+1] + A[i]
    if s > x:
        if A[i+1] >= s-x:
            A[i+1] -= (s-x)
        else:
            t = s-x-A[i+1]
            A[i+1] = 0
            A[i] -= t
print(S - sum(A))