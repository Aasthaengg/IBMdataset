from math import ceil
N = int(input())
L = [list(map(int,input().split())) for k in range(N)]
A, T = 1, 1
for k in range(N):
    a, t = L[k][0], L[k][1]
    m = max(A//a,T//t)
    if a*m < A or t*m < T:
        m += 1
    A = a*m
    T = t*m
print(A+T)
